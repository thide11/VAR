import datetime
import os
import tempfile

from src.converter import MkvConverter
from src.database import Database
from src.ffmpeg import FFmpeg
from src.logger import Logger
from src.s3 import S3
from src.transcriptor import Transcriptor


class Video:
  def __init__(self, file_path, storage_path, transcription_segments):
    self.file_path = file_path
    self.storage_path = storage_path
    self.transcription_segments = transcription_segments

class VideoProcessor:
  def __init__(self):
    self.s3 = S3()
    self.logger = Logger()
    self.converter = MkvConverter()
    self.database = Database()
    self.transcriptor = Transcriptor()
    self.video_manipulator = FFmpeg()


  def start_processor(self, input_folder):
    videos = os.listdir(input_folder)
    self.logger.log(f"Starting video processor with {len(videos)} files")
    for index, file in  enumerate(videos):
      self.process_video(input_folder + "/" + file)
      self.logger.log(f"Processed {index + 1} of {len(videos)} files")


  # Imprimir o conteúdo
  def __read_segment(self, segment):
    id = segment['id']
    startTime = segment['start']
    endTime = segment['end']
    description = segment['text']

    return {
      'id': id,
      'start_time': startTime,
      'transcription': description,
      'end_time': endTime
    }

  def __read_video_transcript_and_save(self, video : Video):
    size = os.path.getsize(video.file_path)
    video_metadata = self.video_manipulator.load_video_metadata(video.file_path)
    if('duration' in video_metadata):
      duration = video_metadata['duration']
    else:
      duration = 0
    data = {
      'date': datetime.datetime.now(),
      'size': size,
      'video_url': video.storage_path,
      'duration': duration,
    }
    meet_id = self.database.save_meet(data)

    for segment in video.transcription_segments:
      block_data = self.__read_segment(segment)
      block_data["meets_id"] = meet_id
      self.database.save_transcription_fragment(block_data)

  def process_video(self, archive_path):
    print(f"Processing video {archive_path}")
    if(archive_path.endswith(".mkv")):
      archive_path = self.converter.convert_to_mp4(archive_path)
    if(not archive_path.endswith(".mp4")):
      self.logger.log(f"Process an file that is not an video detected: {archive_path}")
      return;

    file_name = os.path.basename(archive_path)

    storage_path = "videos/" + file_name
    thumbnail_path = "thumbnails/" + file_name.replace(".mp4", ".jpg")

    if(not self.s3.file_exists(thumbnail_path)):
      self.logger.log("Generating thumbnail...")
      temp_thumnail_path = tempfile.gettempdir() + "/" + file_name.replace(".mp4", ".jpg")
      self.video_manipulator.generate_thumbnail(archive_path, temp_thumnail_path, 720)
      self.s3.upload_file(temp_thumnail_path, thumbnail_path)
      os.remove(temp_thumnail_path)

    if(not self.s3.file_exists(storage_path)):
      self.logger.log("Sending to s3...")
      self.s3.upload_file(archive_path, storage_path)
    
    if(self.database.load_meet_by_path(storage_path) == None):
      self.logger.log("Transcriptiong video...")
      segments = self.transcriptor.transcript(archive_path)
      video = Video(archive_path, storage_path, segments)
      self.__read_video_transcript_and_save(video)
    
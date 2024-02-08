import ffmpeg


class FFmpeg:
  def load_video_metadata(self, input_file_path : str):
    return ffmpeg.probe(input_file_path)['format']
  
  def generate_thumbnail(self, video_input_path : str, image_output_path : str, width : int):
    metadata = self.load_video_metadata(video_input_path)
    time = 0
    if('duration' in metadata):
      time = round(float(metadata['duration']) / 2)
    try:
        (
            ffmpeg
            .input(video_input_path, ss=time)
            .filter('scale', width, -1)
            .output(image_output_path, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
      print(e.stderr.decode(), file=sys.stderr)
      sys.exit(1)
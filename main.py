# import time

# time.sleep(10000)

import re
import datetime

import os
import json

from datetime import date
from src.database import Database
from src.s3 import S3
from src.converter import MkvConverter
from src.transcriptor import Transcriptor
from src.ffmpeg import FFmpeg
from src.video_processor import VideoProcessor

processor = VideoProcessor()
processor.start_processor("D:/Videos")


# database = Database()
# s3 = S3()
# converter = MkvConverter()
# transcriptor = Transcriptor()
# ffmpeg = FFmpeg()


# videos_dir = "D:/Videos"
# videos = os.listdir(videos_dir)
# database_videos = database.list_synced_videos()



# for file in videos:
#   s3_file_name = file.replace(".mkv", ".mp4")
#   s3_path = f"videos/{s3_file_name}"
#   if(file.endswith(".mkv") or file.endswith(".mp4")):
#     converted_file = file.replace(".mkv", ".mp4")

#     filePath = videos_dir + "/" + file
  
#     if(not s3.file_exists(s3_path)):
#        print(f"Enviando vídeo {converted_file}...")
#        output_path = converter.convert_to_mp4(filePath)
#        s3.upload_file(output_path, s3_path=s3_path)

#        print("Vídeo enviado!")
#        print(date.ctime())

#     print((ffmpeg.probe(output_path)['format']["duration"] / 60) + " minutos")
#     if(not (s3_path in database_videos)):
#       output_path = converter.convert_to_mp4(filePath)
#       print(file)
#       print("Convertido para")
#       print(output_path)

#       # if(s3.file_exists(output_path)):
#       #   print("Vídeo já existe na aws...")
#       # else:
#       #   print("Enviando vídeo...")
#       #   s3.upload_video(output_path)
#       #   print("Vídeo enviado!")

#       print("Transcrevendo...")
#       segments = transcriptor.transcript(output_path)
#       with open("dados.json", "w") as arquivo:
#         json.dump(segments, arquivo)

#       print("Vídeo transcrito!")
#       print("Enviando transcrição para o banco...")
#       read_video(output_path, s3_path=s3_path)
#       print("Transcrição enviada!")
#       print(f"Video {output_path} processado.")
#       print(date.ctime())
#     else:
#       print(f"Arquivo já sincronizado: {file}")
#   else:
#     print(f"Arquivo que não é mkv ignorado: {file}")

# print(files)
# read_video()

# print(len(blocks))
# read_block(blocks[100])

# print(read_block(str_block[0]))


# import re
# import datetime

# import os

# from src.database import Database
# from src.s3 import S3
# from src.converter import MkvConverter
# from src.transcriptor import Transcriptor
import ffmpeg

print(ffmpeg.probe("videos/2023-01-13 10-37-28.mp4"))

# database = Database()
# s3 = S3()
# converter = MkvConverter()
# transcriptor = Transcriptor()

# print("Transcrevendo...")
# segments = transcriptor.transcript("D:/OneDrive/programacao/projetos_com_linguagens_variadas/docker/meet_indexer/whisper-diarization/data/recording.mp4")

# print(segments)
# # print(
# #   database.get_raw_transcription(25)
# # )
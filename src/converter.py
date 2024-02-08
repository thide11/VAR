import moviepy.editor as movpy
import os

class MkvConverter:
    def convert_to_mp4(self, path : str):
      output = path.replace(".mkv", ".mp4")
      if(os.path.exists(output)):
        return output
      if(os.path.exists(path)):
        if(path != output):
          os.rename(path, output)
        return output
      print(path)
      print(output)
      raise "Arquivo de entrada e de saida inexistente"
      #video = movpy.VideoFileClip(path)
      #video.write_videofile(path + ".mp4", codec="libx264",audio_codec="aac")
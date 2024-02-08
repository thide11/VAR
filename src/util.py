import os

class Util:
  @staticmethod
  def filename(path):
    return os.path.splitext(os.path.basename(path))[0]
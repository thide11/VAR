from datetime import date
import datetime


class Logger:
  def log(self, message : str):
    now = datetime.datetime.now()
    time = f"{now.hour}:{now.minute}:{now.second}"
    print(f"{time}: {message}")
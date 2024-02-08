import whisper

class Transcriptor:
  def transcript(self, file):
    #tiny, base, small, medium, large
    model = whisper.load_model("medium", device="cuda")
    result = model.transcribe(file)
    return result['segments']

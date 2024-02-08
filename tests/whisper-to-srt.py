from datetime import timedelta
import os
import whisper
import json

def transcribe_audio(path):
    
    arquivo = open("./dados.json", "r")

    # Leia o conteúdo do arquivo
    conteudo = arquivo.read()

    # model = whisper.load_model("base") # Change this to your desired model
    # print("Whisper model loaded.")
    # transcribe = model.transcribe(audio=path)
    # segments = transcribe['segments']
    print(conteudo)
    segments = json.loads(conteudo)
    print(segments)

    arquivo.close()

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if (text[0] == ' ') else text}\n\n"

        srtFilename = os.path.join("SrtFiles", f"output.srt")
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    return srtFilename

transcribe_audio("")
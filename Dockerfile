FROM python:3.11

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install cuda-python

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

COPY . .

CMD [ "python", "main.py" ]

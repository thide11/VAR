from flask import Flask
from flask_cors import CORS

from src.database import Database
from src.s3 import S3

database = Database()

app = Flask(__name__)
CORS(app)

@app.route("/")
def list_videos():
    return database.list_videos()


@app.route("/meet/<int:meet_id>")
def load_meet(meet_id : int):
    print("Carregando reuniao com o id:")
    print(meet_id)
    s3 = S3()
    meet = database.load_meet(meet_id)
    if(meet == None):
        return {"error": "Meet not found"}, 404
    url = s3.get_presigned_url(meet["video_url"])
    meet["video_path"] = meet["video_url"]
    meet["video_url"] = url

    return meet

@app.route("/search/<string:search>")
def search_transcriptions(search : str):
    print("Pesquinsando por:")
    print(search)
    return database.search_transcriptions(search)
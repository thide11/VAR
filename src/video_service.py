class VideoService:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def get_video(self, video_id):
        return self.video_repository.get_video(video_id)

    def save_video(self):
        return self.video_repository.get_videos()
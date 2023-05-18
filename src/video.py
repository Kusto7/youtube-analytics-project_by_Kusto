import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, id_video):
        # self.id_video = id_video
        try:
            self.id_video = id_video
            api_key: str = os.getenv('YT_API_KEY')
            youtube = build('youtube', 'v3', developerKey=api_key)
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=self.id_video
                                                   ).execute()
            if not video_response['items']:
                raise HttpErrorVideo
        except HttpErrorVideo:
            self.id_video = id_video
            self.video_response = None
            self.url = None
            self.title = None
            self.view_count = None
            self.like_count = None
            print("Неверный ID видео")
        else:
            self.video_response = video_response
            self.url = "https://youtu.be/" + self.id_video
            self.title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist


class HttpErrorVideo(Exception):
    pass

import datetime
import os
import isodate
from googleapiclient.discovery import build
from src.video import Video


class PlayList:

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_response = youtube.playlists().list(
                                        part='snippet',
                                        id=self.id_playlist,
                                        maxResults=50)

        playlist_videos = youtube.playlistItems().list(playlistId=self.id_playlist,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        self.playlist_video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()

        self.playlist_videos = playlist_videos
        self.playlist_response = playlist_response.execute()
        self.title = self.playlist_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.id_playlist}'

    @property
    def total_duration(self):
        total_duration_video = datetime.timedelta()
        for video in self.playlist_video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration_video += duration
        return total_duration_video

    def show_best_video(self):
        all_video = []
        for video in self.playlist_videos['items']:
            all_video.append(Video(video["contentDetails"]["videoId"]))
        like_top = 0
        for video in all_video:
            if int(video.like_count) > like_top:
                like_top = int(video.like_count)
                best_video = video.url
        return best_video

import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.channel = channel
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.subscriberCount = channel['items'][0]['statistics']['subscriberCount']
        self.videoCount = channel['items'][0]['statistics']['videoCount']
        self.viewCount = channel['items'][0]['statistics']['viewCount']

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        return print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self):
        with open(f'{self.title}.json', 'w') as file:
            json_channel = ({'id канала': self.__channel_id,
                             'название канала': self.title,
                             'описание канала': self.description,
                             'ссылка на канал': self.url,
                             'количество подписчиков': self.subscriberCount,
                             'количество видео': self.videoCount,
                             'общее количество просмотров': self.viewCount
                             })
            json.dump(json_channel, file, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(cls, channel_id):
        return cls(channel_id)

from src.channel import Channel

if __name__ == '__main__':
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    vdud.print_info()

"""
{
  "kind": "youtube#channelListResponse",
  "etag": "pej8Ui0_rzF1DcBaPaDdR4IwyC4",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "h83A5h44uAHGQr9Me8pwRm3lemo",
      "id": "UCMCgOm8GZkHp8zJ6l7_hIuA",
      "snippet": {
        "title": "вДудь",
        "description": "Здесь задают вопросы",
        "customUrl": "@vdud",
        "publishedAt": "2014-01-03T06:27:22Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqP7ZdK1_dZYqq6_mrzpDPfbrXYCqt-9bUnGVyAI=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqP7ZdK1_dZYqq6_mrzpDPfbrXYCqt-9bUnGVyAI=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqP7ZdK1_dZYqq6_mrzpDPfbrXYCqt-9bUnGVyAI=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "вДудь",
          "description": "Здесь задают вопросы"
        }
      },
      "statistics": {
        "viewCount": "1984417924",
        "subscriberCount": "10300000",
        "hiddenSubscriberCount": false,
        "videoCount": "167"
      }
    }
  ]
}
"""


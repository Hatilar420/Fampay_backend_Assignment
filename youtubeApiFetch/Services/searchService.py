from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from youtubeApiFetch.settings import (
    DEVELOPER_KEYS,
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    DEFAULT_QUERY
)

def YoutubeSearch(query = DEFAULT_QUERY , interval = 1 , max_res = 50 ):
    for i in DEVELOPER_KEYS:
        try:
            youtube = build(
                    YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=i,
            )
            search = youtube.search().list(
                q = query,
                part = 'id,snippet',
                published_After = datetime.now() - timedelta(minutes=interval).isoformat() + 'Z',
                order = 'date',
                max_results = max_res
            ).execute()
            print(search)
            return search
        except HttpError as e :
            Status_Code = e.resp.status
            if Status_Code == 403:
                print("Developer Key {Key} has expired or not working".format(Key = i))
                continue
            print("{code}  : {occured}".format(code = e.resp.status , occured = e.content))
            return None
from youtubeApiFetch.Services.searchService import YoutubeSearch
from youtubeApiFetch.coreApi import models
from dateutil import parser
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

def StoreApiService():
    search_res = YoutubeSearch(interval=2)
    logger.info("Successfully Fetched Videos")
    for item in search_res.get("items", []):
        if all(
            [
                not models.Youtube_Video_Summary.objects.filter(
                    video_id =  item["id"]["videoId"]
                ).exists(),
                item["id"]["kind"] == "youtube#video",
            ]
        ):
            snippet = item["snippet"]
            model_dic = {
                'video_id' :  item["id"]["videoId"],
                'description' : snippet['description'],
                'title' : snippet['title'],
                'thumbnail_url' : snippet["thumbnails"]["default"]["url"],
                'published_on' : parser.parse(snippet["publishedAt"])
            }
            models.Youtube_Video_Summary(**model_dic).save()
    logger.info("Successfully Updated Videos DB")
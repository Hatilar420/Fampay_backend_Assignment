from youtubeApiFetch.Services.searchService import YoutubeSearch
from youtubeApiFetch.coreApi import models
from dateutil import parser

def StoreApiService():
    search_res = YoutubeSearch(interval=2, max_res=25)
    # logger.info("Successfully Fetched Videos")
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
            models.Youtube_Video_Summary(**model_dic)
            models.Youtube_Video_Summary.save()
    # logger.info("Successfully Updated Videos DB")
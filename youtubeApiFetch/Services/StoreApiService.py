from Services.searchService import YoutubeSearch
from fetchApi.models import models as core_model
from youtubeApiFetch.Domain import CommonDomain
from dateutil import parser

Video_Summary_Domain = CommonDomain(core_model.Youtube_Video_Summary)

def StoreApiService():
    search_res = YoutubeSearch(interval=2, max_res=25)
    # logger.info("Successfully Fetched Videos")
    for item in search_res.get("items", []):
        if all(
            [
                not core_model.Youtube_Video_Summary.objects.filter(
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
            Video_Summary_Domain.create(model_dic)
    # logger.info("Successfully Updated Videos DB")
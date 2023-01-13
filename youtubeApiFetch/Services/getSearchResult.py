from youtubeApiFetch.coreApi import models
from django.db.models import Q

Video_Summary = models.Youtube_Video_Summary

def GetSearchResultByPublishOrder(query):
    # split the query by space
    query_list = query.split()
    query_list = [x for x in query_list if x]
    # create a Q object for each word in the query
    q_objects = [Q(title__icontains=word) | Q(description__icontains=word) for word in query_list]
    # take the Q objects and join them with OR
    q_objects_or = q_objects.pop()
    for obj in q_objects:
        q_objects_or |= obj
    videos = Video_Summary.objects.filter(q_objects_or).order_by('-published_on')
    return videos

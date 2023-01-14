from rest_framework.response import Response
from rest_framework.decorators import api_view
from youtubeApiFetch.Services.getSearchResult import GetSearchResultByPublishOrder
from youtubeApiFetch.coreApi.VideoSerializer import VideoSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.
@api_view(["GET"])
def video_collection(request):
    Search_query = request.GET.get('search')
    if(Search_query == None):
        return Response(status=400,data="Please specify search query")
    paginator = PageNumberPagination()
    res = GetSearchResultByPublishOrder(Search_query)
    context = paginator.paginate_queryset(res, request)
    serial_data = VideoSerializer(context,many=True)
    return paginator.get_paginated_response(data=serial_data.data)
from django.http import JsonResponse
from rest_framework.decorators import api_view
from youtubeApiFetch.Services.getSearchResult import GetSearchResultByPublishOrder
from youtubeApiFetch.coreApi.VideoSerializer import VideoSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.
@api_view(["GET"])
def video_collection(request):
    Search_query = request.GET.get('search')
    if(Search_query == None):
        return JsonResponse(status=400,data="Please specify search query")
    paginator = self.pagination_class()
    res = GetSearchResultByPublishOrder(Search_query)
    
    serial_data = VideoSerializer(res.all(),many=True)
    return JsonResponse(data=serial_data.data, status=200,safe=False)
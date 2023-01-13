from rest_framework import response
from rest_framework.decorators import api_view
from youtubeApiFetch.Services.StoreApiService import StoreApiService


# Create your views here.
@api_view(["GET"])
def video_collection(request):
    StoreApiService()
    return response(status=200)
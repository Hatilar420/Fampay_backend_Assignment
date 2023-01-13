from rest_framework import serializers
from youtubeApiFetch.coreApi.models import Youtube_Video_Summary


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube_Video_Summary
        fields = (
            "id",
            "video_id",
            "title",
            "description",
            "published_on",
            "thumbnail_url",
        )

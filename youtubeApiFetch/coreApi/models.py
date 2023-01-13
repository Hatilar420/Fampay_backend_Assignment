from django.db import models

class Youtube_Video_Summary(models.Model):
    video_id = models.CharField(max_length=255, unique = True)
    title = models.CharField("title of the video", max_length=255)
    description = models.TextField("Description of the video")
    thumbnail_url = models.URLField(
        "Image URL", max_length=255,
    )
    published_on = models.DateTimeField("publishing datetime")

    def __str__(self):
        return self.title


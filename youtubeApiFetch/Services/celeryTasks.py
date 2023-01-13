# from celery import task
from youtubeApiFetch.Services.StoreApiService import StoreApiService

# @task(default_retry_delay=30, max_retries=3, soft_time_limit=10000)
# 
from celery import Celery
from datetime import timedelta

celery = Celery(__name__)
celery.config_from_object(__name__)

@celery.task
def collect_videos():
    StoreApiService()
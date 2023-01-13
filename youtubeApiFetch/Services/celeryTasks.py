from celery import shared_task as task
from youtubeApiFetch.Services.StoreApiService import StoreApiService

@task(default_retry_delay=30, max_retries=3, soft_time_limit=10000)
def collect_videos():
    StoreApiService()

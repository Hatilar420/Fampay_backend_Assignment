from datetime import timedelta
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "collect_videos": {
        "task": "youtubeApiFetch.Services.celeryTasks.collect_videos",
        "schedule": crontab(minute='*/2'),
    }
}

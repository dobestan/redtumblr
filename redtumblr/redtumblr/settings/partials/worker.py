import os

from celery.schedules import crontab


BROKER_URL = os.environ.get(
    'BROKER_URL',
    'redis://localhost:6379/0',
)


CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CELERYBEAT_SCHEDULE = {
    'Tumblr | Update Blog Feeds': {
        'task': 'tumblr.tasks.feed.UpdateBlogFeedTask',
        'schedule': crontab(
            hour='18',
        )
    },

    'Tumblr | Update Blog Status': {
        'task': 'tumblr.tasks.status.UpdateBlogStatusTask',
        'schedule': crontab(
            hour='18',
        )
    },
}


CELERY_TIMEZONE = 'Asia/Seoul'


# Celery Custom Settings
# http://celery.readthedocs.org/en/latest/configuration.html

CELERY_APP = "redtumblr.celery:app"

CELERY_IGNORE_RESULT = True

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracker_project.settings')
app = Celery('tracker_project')


class Config:
    timezone = 'Asia/Kolkata'
    enable_utc = True

    task_always_eager = False
    broker_url = 'redis://:@127.0.0.1:6379/13'
    result_expires = 3600
    worker_prefetch_multiplier = 1
    worker_max_memory_per_child = 250000  # 250MB

    beat_schedule = {
        'task_daily_update': {
            'task': 'celery_config.send_email_notifications',
            'schedule': crontab(),
            'args': (),
        },
        'task_weekly_update': {
            'task': 'celery_config.send_email_notifications',
            'schedule': crontab(),
            'args': (),
        },
        'task_monthly_update': {
            'task': 'celery_config.send_email_notifications',
            'schedule': crontab(),
            'args': (),
        },
    }
    worker_hijack_root_logger = False
    accept_content = ['json']



# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
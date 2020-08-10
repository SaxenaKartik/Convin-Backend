from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from tracker_api import models 
from datetime import datetime

logger = get_task_logger(__name__)


@periodic_task(
	run_every=(crontab(0, hour = 17)),
	name="task_daily_update",
	ignore_result=True
)
def task_daily_update():
	""" 
		send email daily 
	"""

	trackers = models.TaskTracker.objects.filter(update_type = 1).values_list("id", "task_type", "email")
	for tracker in trackers:
		tracker_id = tracker[0]
		tracker_task_type = tracker[1]
		tracker_email = tracker[2]

		# find list of tasks updated in last 24 hours 
		tracker_list_tasks = models.Task.objects.filter(created_on__gt = datetime.today()-datetime.timedelta(days=1), task_type = tracker_task_type).values()

		# send mails

	logger.info("Daily Emails Sent!")


@periodic_task(
	run_every=(crontab(0,0,day_of_week='1')),
	name="task_weekly_update",
	ignore_result=True
)
def task_weekly_update():
	""" 
		send email weekly 
	"""

	trackers = models.TaskTracker.objects.filter(update_type = 2).values_list("id", "task_type", "email")


	for tracker in trackers:
		tracker_id = tracker['id']
		tracker_task_type = tracker['task_type']
		tracker_email = tracker['email']
		# find list of tasks updated in last week 
		tracker_list_tasks = models.Task.objects.filter(created_on__gt = datetime.today()-datetime.timedelta(days = 7), task_type = tracker_task_type).values()

		# send mails

	logger.info("Weekly Emails Sent!")

@periodic_task(
	run_every=(crontab(0, 0, day_of_month='1')),
	name="task_monthly_update",
	ignore_result=True
)
def task_monthly_update():
	""" 
		send email monthly
	"""

	trackers = models.TaskTracker.objects.filter(update_type = 3).values_list("id", "task_type", "email")

	for tracker in trackers:
		tracker_id = tracker[0]
		tracker_task_type = tracker[1]
		tracker_email = tracker[2]

		# find list of tasks updated in last month 
		tracker_list_tasks = models.Task.objects.filter(created_on__gt = (datetime.today().replace(day=1)-datetime.timedelta(days=1)).replace(day=1), task_type = tracker_task_type).values()

		# send mails

	logger.info("Monthly Emails Sent!")
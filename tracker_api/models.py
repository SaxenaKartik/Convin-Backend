from django.db import models

# Choices for task type

TASK_TYPE_CHOICES = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
)

# Choices for update type

UPDATE_TYPE_CHOICES = (
	(1, "Daily"),
	(2, "Weekly"),
	(3, "Monthly"),
)


class Task(models.Model):
	""" Model for tasks """

	task_type = models.IntegerField(choices = TASK_TYPE_CHOICES)
	task_desc = models.CharField(max_length = 100)
	created_on = models.DateTimeField(auto_now_add = True)

	def get_desc(self):
		""" Function to return task description """
		return self.task_desc

	def __str__(self):
		""" Function to return object name """
		return "Task Id : " + str(self.id) + " Task Type : " + str(self.get_task_type_display()) + "Created On : " + str(self.created_on)

	class Meta:

		verbose_name_plural = "Tasks"

class TaskTracker(models.Model):
	""" Model for task trackers"""

	task_type = models.IntegerField(choices = TASK_TYPE_CHOICES)
	update_type = models.IntegerField(choices = UPDATE_TYPE_CHOICES)
	email = models.EmailField(max_length =254)

	def get_email(self):
		""" Function to return email id registered with the tracker """
		return self.email

	def __str__(self):
		""" Function to return object name """
		return "Tracker Id : " + str(self.id) + " Task Type : " + str(self.get_task_type_display()) + " Update Type : " + str(self.get_update_type_display())

	class Meta:

		verbose_name_plural = "TaskTrackers"
from rest_framework import serializers
from tracker_api import models

class TaskSerializer(serializers.ModelSerializer):
    """Serializes fields for Task Model"""

    class Meta :
        model = models.Task
        fields = ("id","task_type","task_desc")

class TaskTrackerSerializer(serializers.ModelSerializer):
	""" Serializes fields of TaskTracker Model """

	class Meta :
		model = models.TaskTracker
		fields = ("id", "task_type", "update_type", "email")
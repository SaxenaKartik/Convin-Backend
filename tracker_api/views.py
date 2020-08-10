from django.shortcuts import render
from rest_framework import viewsets
from tracker_api import models
from tracker_api import serializers

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating task"""

    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class TaskTrackerViewSet(viewsets.ModelViewSet):
	""" Handle creating and updating task tracker"""

	serializer_class = serializers.TaskTrackerSerializer
	queryset = models.TaskTracker.objects.all()

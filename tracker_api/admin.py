from django.contrib import admin
from tracker_api import models
# Register your models here.

admin.site.register(models.Task)
admin.site.register(models.TaskTracker)
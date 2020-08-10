from django.urls import path, include
from tracker_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task', views.TaskViewSet)
router.register('tasktracker', views.TaskTrackerViewSet)


urlpatterns = [
	path('', include(router.urls))
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TermViewSet,
    CourseViewSet,
    ScheduleViewSet,
    AnnouncementViewSet,
    LectureResourceViewSet,
)

router = DefaultRouter()
router.register(r'terms', TermViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'resources', LectureResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import viewsets
from .models import Term, Course, Schedule, Announcement, LectureResource
from .serializers import (
    TermSerializer,
    CourseSerializer,
    ScheduleSerializer,
    AnnouncementSerializer,
    LectureResourceSerializer,
)


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class LectureResourceViewSet(viewsets.ModelViewSet):
    queryset = LectureResource.objects.all()
    serializer_class = LectureResourceSerializer

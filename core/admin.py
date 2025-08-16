from django.contrib import admin
from .models import Term, Course, Schedule, Announcement, LectureResource

admin.site.register(Term)
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(Announcement)
admin.site.register(LectureResource)

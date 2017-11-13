from django.contrib import admin

from .models import Lesson, LessonPart

admin.site.register(Lesson)
admin.site.register(LessonPart)
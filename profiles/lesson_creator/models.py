from django.db import models

from profiles.models import TeacherProfile


class LessonCreator(models.Model):

    teacher = models.OneToOneField(TeacherProfile)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # lessons_created = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.teacher.get_name_or_username()

from django.contrib.auth.models import User
from django.db import models

from profiles.models import LessonCreator
from profiles.models import TeacherProfile, StudentProfile


class BaseLesson(models.Model):

    STARTED = 'ST'          # DEFAULT
    FINISHED = 'FI'         # LESSON CREATOR HAS PRESSED THE 'FINISHED' BUTTON
    SECOND_CHECK = 'SC'     # SECOND CHECK HAS BEEN PERFORMED BY ANOTHER LESSON CREATOR
    APPROVED = 'AP'         # APPROVED BY ADMIN

    STATUS_CHOICES = (
        (STARTED, 'Started'),
        (FINISHED, 'Finished'),
        (SECOND_CHECK, 'Second Check'),
        (APPROVED, 'Approved'),
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    lesson_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STARTED,)

    created_by = models.ForeignKey(
        LessonCreator,
        on_delete=models.SET_NULL,
        related_name='created_by',
        default=None,
        null=True,
    )
    updated_by = models.ForeignKey(
        LessonCreator,
        on_delete=models.SET_NULL,
        related_name='updated_by',
        default=None,
        null=True,
        blank=True,

    )
    second_checked_by = models.ForeignKey(
        LessonCreator,
        on_delete=models.SET_NULL,
        related_name='second_checked_by',
        default=None,
        null=True,
        blank=True,

    )
    approved_by = models.ForeignKey(
        LessonCreator,
        on_delete=models.SET_NULL,
        related_name='approved_by',
        default=None,
        null=True,
        blank=True,

    )

    class Meta:
        abstract = True


# @python_2_unicode_compatible
class Lesson(models.Model):

    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class LessonPart(BaseLesson):

    lesson = models.ForeignKey(Lesson, default=None)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    media_url = models.URLField(blank=True)
    media_caption = models.TextField(blank=True)

    def __str__(self):
        return self.title


# TODO
'''
    When user creates a lesson:
    # Choose a name for the lesson, can be changed later
    # User is given the option to create a new lessons part
    # Start filling in the info for the first lessons part - relationship with lesson
    # Lesson part info: Name, description, media URL, media caption
'''
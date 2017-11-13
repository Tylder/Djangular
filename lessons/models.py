from django.db import models

# Create your models here.

# @python_2_unicode_compatible
class Lesson(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LessonPart(models.Model):

    lesson = models.ForeignKey(Lesson, default=None)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    media_url = models.URLField(blank=True)
    media_caption = models.TextField(blank=True)

    def __str__(self):
        return self.title
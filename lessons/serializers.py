from rest_framework import serializers
from .models import Lesson, LessonPart


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
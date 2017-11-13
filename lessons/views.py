from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LessonSerializer
from .models import Lesson


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)
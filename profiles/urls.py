from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import TeacherViewSet, StudentViewSet, LessonCreatorViewSet


router = DefaultRouter()
router.register(r'teacher/lesson-creator', LessonCreatorViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)


# router.register(r'rank', TeacherByRank.as_view(), 'rank')

urlpatterns = router.urls

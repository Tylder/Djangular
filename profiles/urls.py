from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, LessonCreatorViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'teacher/lesson-creator', LessonCreatorViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)

# urlpatterns = [
#     url(r'^teacher/$', TeacherDetails.as_view(), name='rest_teacher_details'),
# ]
# router.register(r'rank', TeacherByRank.as_view(), 'rank')

urlpatterns = router.urls

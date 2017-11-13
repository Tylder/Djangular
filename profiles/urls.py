from .views import TeacherViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)
# router.register(r'rank', TeacherByRank.as_view(), 'rank')

urlpatterns = router.urls

from .views import LessonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LessonViewSet)


urlpatterns = router.urls
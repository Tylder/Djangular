#from django.conf.urls import url
#from .api import ListApi, CardApi

#urlpatterns = [

#    # as_view because a view must a function and as_view make a function from a class, 
#    # since ListApi is a class so that we can inherit from rest_framework
#    url(r'^lists$', ListApi.as_view()),    
#    url(r'^cards$', CardApi.as_view()),    

#]


from .views import ListViewSet, CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = router.urls

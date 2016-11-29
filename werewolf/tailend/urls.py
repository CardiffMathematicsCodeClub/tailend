from django.conf.urls import url, include
from rest_framework import routers
from tailend import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'game', views.GameViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
              ]

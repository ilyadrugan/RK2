from django.urls import path, include
from .views_api import OrchestraListAPIView, MusicianListAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'orchestras', OrchestraListAPIView)
router.register(r'musicians', MusicianListAPIView)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
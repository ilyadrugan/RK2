from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include('api.urls')),
    path('orchestra/<int:id>/', views.GetOrchestra, name='orchestra_url')
]
from django.urls import path
from . import views

app_name = 'media_uploads'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('upload/', views.upload_media, name='upload_media'),
    path('media/<int:pk>/', views.media_detail, name='media_detail'),
    path('media/<int:pk>/delete/', views.delete_media, name='delete_media'),
]









from django.urls import path, include
from comments import views


urlpatterns = [
    path('<str:pk>/', views.video_comments),
    path('', views.post_comment),
]
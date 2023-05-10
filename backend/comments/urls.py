from django.urls import path, include
from comments import views


urlpatterns = [
    path('<str:pk>/', views.video_comments),
    path('post/', views.post_comment),
]
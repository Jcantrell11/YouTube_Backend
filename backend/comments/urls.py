from django.urls import path, include
from comments import views


# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

# def dynamic_lookup_view(request, video_id):
#     obj = Comment.objects.get(video_id=video_id)
#     return render(request, obj )

urlpatterns = [
    path('<str:pk>/', views.video_comments),
    path('post/', views.post_comment),
    # path('dhu78sd5/', views.video_comments),
    
]
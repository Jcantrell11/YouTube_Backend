from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.

# def dynamic_lookup_view(request, video_id):
#     obj = Comment.objects.get(video_id=video_id)
#     return render(request, obj )

@api_view(['GET'])
@permission_classes([AllowAny])
def video_comments(request, pk):
    # all_comments = Comment.objects.all()

    # for comment in all_comments:
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    comments = Comment.objects.filter(video_id=pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
    

    # comments = Comment.objects.all()
    # serializer = CommentSerializer(comments, many=True)
    # return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
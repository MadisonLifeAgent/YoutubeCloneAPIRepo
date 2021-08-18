from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.
class CommentList(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CommentDetail(APIView):
#     def get(self, request, id):
#         comment = Comment.objects.get(pk=id)
#         if comment:
#             serializer = CommentSerializer(comment)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)

# class CommentLikes(APIView):
#     def get(self, request, id):
#         song = Song.objects.get(pk=id)
#         if song:
#             serializer = SongSerializer(song)
#             serializer.like(song)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)

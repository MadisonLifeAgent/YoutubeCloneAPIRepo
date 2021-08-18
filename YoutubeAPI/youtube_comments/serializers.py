from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['videoId', 'body', 'likes', 'dislikes', 'parentComment']

    def like(self, instance):
        instance.likes += 1
        instance.save()
        return instance

    def dislike(self, instance):
        instance.dislikes += 1
        instance.save()
        return instance
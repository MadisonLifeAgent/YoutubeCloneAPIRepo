from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Comment(models.Model):
    videoId = models.CharField(max_length=11, default=0)
    body = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    parentComment = models.ForeignKey('youtube_comments.Comment', blank=True, null=True, on_delete=CASCADE)

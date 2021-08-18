from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:id>', views.CommentDetail.as_view()),
    path('video/<str:video_id>', views.CommentList.as_view()),
    path('comment/dislike/<int:id>', views.CommentDislikes.as_view()),
    path('comment/like/<int:id>', views.CommentDislikes.as_view())
]
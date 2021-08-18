from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:id>', views.CommentDetail.as_view()),
    path('video/<str:video_id>', views.CommentList.as_view())
]
from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.CommentList.as_view())
]
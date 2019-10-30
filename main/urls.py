from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='main-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='main-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]

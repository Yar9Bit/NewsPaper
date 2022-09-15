from django.urls import path
from .views import PostView, PostDetail, SearchView, CreatePost, UpdatePost, DeletePost

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', SearchView.as_view()),
    path('add/', CreatePost.as_view(), name='post_create'),
    path('<int:pk>/edit', UpdatePost.as_view(), name='post_edit'),
    path('<int:pk>/delete', DeletePost.as_view(), name='post_delete')
]

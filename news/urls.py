from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (PostView,
                    PostDetail,
                    SearchView,
                    CreatePost,
                    UpdatePost,
                    DeletePost,
                    subscribe_category,
                    )

urlpatterns = [
    path('', cache_page(60*1)(PostView.as_view())),
    path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('search/', SearchView.as_view()),
    path('add/', CreatePost.as_view(), name='post_create'),
    path('<int:pk>/edit', UpdatePost.as_view(), name='post_edit'),
    path('<int:pk>/delete', DeletePost.as_view(), name='post_delete'),
    path('subscribe/<int:pk>', subscribe_category, name='sub_category'),
]

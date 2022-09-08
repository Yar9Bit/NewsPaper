import datetime

from django.views.generic import ListView, DetailView
from .models import Post


class PostView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-dateCreate')


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

from django_filters import FilterSet
from .models import Post


class PostFilters(FilterSet):
    class Meta:
        model = Post
        fields = {
            'dateCreate': ['gt'],
            'title': ['icontains'],
            'author': ['exact']
        }

from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Post, Category, User, CategorySubscribe, PostCategory
from .filters import PostFilters
from .forms import PostForm
from django.core.cache import cache
from django.contrib.auth.decorators import login_required


class PostView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-dateCreate']
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilters(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None, *args, **kwargs):
        obj = cache.get(f'News-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super(PostDetail, self).get_object(queryset=self.queryset)
            cache.set(f'News-{self.kwargs["pk"]}', obj)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = context['object'].id
        user_id = self.request.user.id
        category = PostCategory.objects.filter(categoryThrough_id=post_id)
        user_category = CategorySubscribe.objects.filter(subscriber_thru_id=user_id)
        context['is_not_subscribe'] = not user_category.exists()
        # проверить, на какие категории еще не подписан

        not_subscribe_category = []
        for cat in category:
            if cat.categoryThrough_id not in user_category.values_list('category_thru_id', flat=True):
                not_subscribe_category.append(cat)
        context['category'] = not_subscribe_category
        return context


class SearchView(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'post_search'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilters(self.request.GET, queryset=self.get_queryset())
        return context


class CreatePost(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'post_create.html'
    permission_required = 'news.add_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context


class UpdatePost(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'post_edit.html'
    form_class = PostForm
    permission_required = 'news.change_post'

    def get_object(self, queryset=None, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class DeletePost(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'news.delete_post'
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


@login_required
def subscribe_category(request, pk):
    user = [User.objects.get(pk=request.user.id)]
    category = Category.objects.get(pk=pk)
    category.subscribers.set(user)
    return redirect('/news/')

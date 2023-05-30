from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


def pet_sitter_required(user):
    return user.is_authenticated and user.is_pet_sitter


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(pet_sitter_required), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_new')


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(pet_sitter_required), name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(pet_sitter_required), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

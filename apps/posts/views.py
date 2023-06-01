from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.user.models import Location
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from django.http import Http404


def pet_sitter_required(user):
    return user.is_authenticated and user.is_pet_sitter


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        location = self.request.GET.get('location', '')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if location:
            queryset = queryset.filter(user__location__id=location)

        return queryset



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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(pet_sitter_required), name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        qs = super().get_queryset()
        # Solo permite a los usuarios editar sus propios posts.
        return qs.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise Http404("No estás autorizado para editar este Post")
        return super().dispatch(request, *args, **kwargs)



@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(pet_sitter_required), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

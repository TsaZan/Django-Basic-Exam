from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from furryFunnies.author.forms import AuthorCreateForm, AuthorEditForm
from furryFunnies.author.models import Author
from furryFunnies.post.models import Post
from furryFunnies.utils import get_author


class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('dashboard')


class AuthorDetailsView(TemplateView):
    model = Author
    template_name = 'author/details-author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_author()
        context['posts_count'] = Post.objects.all().count()
        context['posts'] = Post.objects.all().order_by('updated_at')
        return context


class EditAuthorView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'author/edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self):
        return get_author()


class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return get_author()

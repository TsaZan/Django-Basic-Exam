from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from furryFunnies.author.models import Author
from furryFunnies.mixins import ReadOnlyFields
from furryFunnies.post.forms import PostCreateForm, PostDeleteForm, PostEditForm
from furryFunnies.post.models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = Author.objects.last()
        return super().form_valid(form)


class DetailsPostView(DetailView):
    model = Post
    fields = '__all__'
    template_name = 'post/details-post.html'
    pk_url_kwarg = 'id'


# Create your views here.
class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post/edit-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dashboard')


class DeletePostView(ReadOnlyFields, DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'post/delete-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        initial = super().get_initial()
        initial['title'] = self.object.title
        initial['image_url'] = self.object.image_url
        initial['content'] = self.object.content
        return initial

    def form_invalid(self, form):
        return self.form_valid(form)

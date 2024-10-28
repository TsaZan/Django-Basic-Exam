from django.shortcuts import render
from django.views.generic import TemplateView

from furryFunnies.post.models import Post


class IndexView(TemplateView):
    template_name = 'common/index.html'


class DashboardView(TemplateView):
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

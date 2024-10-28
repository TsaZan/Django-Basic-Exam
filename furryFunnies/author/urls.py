from django.urls import path

from furryFunnies.author.views import CreateAuthorView, EditAuthorView, DeleteAuthorView, AuthorDetailsView

urlpatterns = [
    path('create/', CreateAuthorView.as_view(), name='author-create'),
    path('details/', AuthorDetailsView.as_view(), name='author-details'),
    path('edit/', EditAuthorView.as_view(), name='author-edit'),
    path('delete/', DeleteAuthorView.as_view(), name='author-delete'),
]

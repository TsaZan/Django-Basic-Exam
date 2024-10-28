from django.urls import path, include
from furryFunnies.post.views import EditPostView, DetailsPostView, PostCreateView, DeletePostView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create-post'),

    path('', include([
        path('<int:id>/', include([
            path('details/', DetailsPostView.as_view(), name='details-post'),
            path('edit/', EditPostView.as_view(), name='edit-post'),
            path('delete/', DeletePostView.as_view(), name='delete-post')
        ]))
    ])),

]

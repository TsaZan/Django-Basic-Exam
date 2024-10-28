
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('furryFunnies.common.urls')),
    path('posts/', include('furryFunnies.post.urls')),
    path('author/', include('furryFunnies.author.urls')),
    path('admin/', admin.site.urls),

]

from django.urls import path
from justPost.views import indexView, allPostsView

urlpatterns = [
    path('', indexView, name='home'),
    path('posts/', allPostsView, name='posts')
]
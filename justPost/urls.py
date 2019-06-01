from django.urls import path
from django.conf.urls import url
from justPost.views import indexView, allPostsView, authorPostsView

urlpatterns = [
    path('', indexView, name='home'),
]
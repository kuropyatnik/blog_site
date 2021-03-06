"""blog_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from justPost.views import signupView, loginView, logoutView
from justPost.views import indexView, allPostsView, authorPostsView, singlePostView, feedPostsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('justPost.urls')),
    url(r'^signup/$', signupView, name='signup'),
    url(r'^login/$', loginView, name='login'),
    url(r'^logout/$', logoutView, name='logout'),
    path('home/', include('justPost.urls')),
    path('posts/', allPostsView, name='posts'),
    path('feed/', feedPostsView, name='feed'),
    url(r'^author/(?P<stub>[-\w]+)$', authorPostsView, name='author'),
    url(r'^post/(?P<pk>\d+)$', singlePostView, name='single-post'),

]

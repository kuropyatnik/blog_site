from django.urls import path
from justPost.views import indexView

urlpatterns = [
    path('', indexView, name='home'),
]
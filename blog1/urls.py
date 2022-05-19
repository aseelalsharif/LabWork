from . import views
from django.urls import path

urlpatterns = [
    path('Blog', views.Blogg, name='Blog'),
]
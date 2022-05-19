from . import views
from django.urls import path

urlpatterns = [
      path('Malaysia', views.Malaysia, name='Malaysia'),
      path('Turkey', views.Turkey, name='Turkey')
]
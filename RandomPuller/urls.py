from django.urls import path

from django.urls import path

from . import views

app_name = 'RandomPuller'

urlpatterns = [
    path('', views.index, name='index'),
]


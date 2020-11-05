from django.urls import path

from . import views

app_name = 'RandomPuller'

urlpatterns = [
    path('', views.index, name='index'),
    path('random_puller/', views.random_puller, name='random_puller'),
]


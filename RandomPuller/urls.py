from django.urls import path

from . import views

app_name = 'RandomPuller'

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<slug:name_of_company>/', views.company_employees, name='company_employees'),
]


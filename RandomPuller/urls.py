from django.urls import path

from . import views

app_name = 'RandomPuller'

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<int:pk>/', views.company_employees, name='company_employees'),
    path('new/company/', views.new_company, name='new_company'),
    path('add/company', views.add_company, name='add_company'),
    path('delete/company/<int:pk>', views.delete_company, name='delete_company'),
    path('update/company/<int:pk>/', views.update_company, name='update_company'),
    path('update/company/<int:pk>/redirect', views.company_update_redirect, name='company_update_redirect'),
    path('new/company/employee/<int:pk>/', views.new_employee, name='new_employee'),
    path('add/employee/<int:pk>', views.add_employee, name='add_employee'),
    path('delete/employee/<int:pk>', views.delete_employee, name='delete_employee'),
    path('pull/<int:pk>', views.pull_randoms, name='pull_randoms'),
    path('pulled/<int:pk>/<uuid:id>/', views.pulled_randoms, name='pulled_randoms'),
    path('pulled/', views.all_pulled, name='all_pulled'),
]

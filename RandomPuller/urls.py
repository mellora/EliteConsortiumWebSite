from django.urls import path

from . import views

app_name = 'RandomPuller'

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<slug:name_of_company>/', views.company_employees, name='company_employees'),
    path('new/company/', views.new_company, name='new_company'),
    path('add/company', views.add_company, name='add_company'),
    path('delete/company/<int:pk>', views.delete_company, name='delete_company'),
    path('new/company/employee/<int:pk>/', views.new_employee, name='new_employee'),
    path('add/employee/<int:pk>', views.add_employee, name='add_employee'),
    path('delete/employee/<int:pk>', views.delete_employee, name='delete_employee'),
]

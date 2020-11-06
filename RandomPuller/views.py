from django.shortcuts import render, redirect, reverse

import random

from .models import Company, Employee


# Create your views here.
def index(request):
    companies = Company.objects.all()

    context = {
        'companies': companies,
    }
    return render(request, 'RandomPuller/index.html', context)


def company_employees(request, name_of_company):
    company_name = name_of_company.replace('_', ' ')
    company = Company.objects.filter(name=company_name).first()
    employees = Employee.objects.filter(company_name=company)

    context = {
        'company': company,
        'employees': employees,
    }
    return render(request, 'RandomPuller/company_employees.html', context)


def add_company(request):
    pass


def delete_company(request, pk):
    Company.objects.filter(pk=pk).delete()
    return redirect('RandomPuller:index')


def add_employee(request):
    pass


def delete_employee(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    company = Company.objects.filter(pk=employee.company_name.pk).first()
    Employee.objects.filter(pk=pk).delete()
    return redirect('RandomPuller:company_employees', name_of_company=company.name.replace(' ', '_'))

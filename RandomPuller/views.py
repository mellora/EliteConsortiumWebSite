from django.shortcuts import render, redirect, reverse

import random

from .models import Company, Employee

SHUFFLE_NUMBER = 5


# Create your views here.
def index(request):
    companies = Company.objects.all()

    context = {
        'companies': companies,
    }
    return render(request, 'RandomPuller/index.html', context)


def company_employees(request, name_of_company):
    if request.method == 'POST':
        company_name = name_of_company.replace('_', ' ')
        company = Company.objects.filter(name=company_name).first()
        employees = Employee.objects.filter(company_name=company)
    else:
        company = None
        employees = None
    context = {
        'company': company,
        'employees': employees,
    }
    return render(request, 'RandomPuller/company_employees.html', context)

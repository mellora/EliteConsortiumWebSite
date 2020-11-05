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


def random_puller(request):
    if request.method == 'POST':
        selected_company_name = request.POST.get('company_select')
        selected_company = Company.objects.filter(name=selected_company_name).first()
        employee_list = Employee.objects.filter(company_name__name=selected_company_name)
    else:
        selected_company = None
        employee_list = None

    companies = Company.objects.all()

    context = {
        'companies': companies,
        'employees': employee_list,
        'selected_company': selected_company,
    }
    return render(request, 'RandomPuller/random_puller.html', context)


def pulled_employees(request):
    if request.method == 'POST':
        try:
            rand_pull = int(request.POST.get('random_number_to_pull'))
        except ValueError:
            rand_pull = 0
        try:
            alt_pull = int(request.POST.get('alternate_number_to_pull'))
        except ValueError:
            alt_pull = 0
        company_name = request.POST.get('company_name')
    else:
        rand_pull = 0
        alt_pull = 0
        company_name = None

    employee_list = list(Employee.objects.filter(company_name__name=company_name))

    if rand_pull + alt_pull >= len(employee_list):
        return redirect('/random/')

    for _ in range(SHUFFLE_NUMBER):
        random.shuffle(employee_list)

    random_employee_list = []
    for pull in range(rand_pull):
        random_employee_list.append(employee_list.pop(0))

    alternate_employee_list = []
    for pull in range(alt_pull):
        alternate_employee_list.append(employee_list.pop(0))

    context = {
        'company': company_name,
        'random_list': random_employee_list,
        'alternate_list': alternate_employee_list,
    }
    return render(request, 'RandomPuller/pulled_employees.html', context)

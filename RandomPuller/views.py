from django.shortcuts import render, redirect

import random

from .models import Company, Employee, PulledRandoms
from .forms import CompanyForm, EmployeeForm


# Create your views here.
def index(request):
    companies = Company.objects.all()

    context = {
        'companies': companies,
    }
    return render(request, 'RandomPuller/index.html', context)


def company_employees(request, pk):
    company = Company.objects.filter(pk=pk).first()
    employees = Employee.objects.filter(company=company)

    context = {
        'company': company,
        'employees': employees,
    }
    return render(request, 'RandomPuller/company_employees.html', context)


def new_company(request):
    c_form = CompanyForm
    context = {
        'form': c_form,
    }
    return render(request, 'RandomPuller/add_company.html', context)


def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = Company()
            company.name = form.cleaned_data['name']
            company.number_of_randoms = form.cleaned_data['number_of_randoms']
            company.number_of_alternates = form.cleaned_data['number_of_alternates']
            company.save()
            return redirect('RandomPuller:index')
    return redirect('RandomPuller:new_company')


def delete_company(request, pk):
    Company.objects.filter(pk=pk).delete()
    return redirect('RandomPuller:index')


def new_employee(request, pk):
    company = Company.objects.filter(pk=pk).first()
    e_form = EmployeeForm
    context = {
        'company': company,
        'form': e_form,
    }
    return render(request, 'RandomPuller/add_employee.html', context)


def add_employee(request, pk):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            company = Company.objects.filter(pk=pk).first()
            employee = Employee()
            employee.first_name = form.cleaned_data['first_name']
            employee.last_name = form.cleaned_data['last_name']
            employee.company = company
            employee.save()
            return redirect('RandomPuller:company_employees', pk=company.pk)
    return redirect('RandomPuller:new_employee')


def delete_employee(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    company = Company.objects.filter(pk=employee.company.pk).first()
    Employee.objects.filter(pk=pk).delete()
    return redirect('RandomPuller:company_employees', pk=company.pk)


def update_company(request, pk):
    company = Company.objects.filter(pk=pk).first()
    c_form = CompanyForm(
        initial={
            'name': company.name,
            'number_of_randoms': company.number_of_randoms,
            'number_of_alternates': company.number_of_alternates,
        }
    )
    context = {
        'company': company,
        'form': c_form,
    }
    return render(request, 'RandomPuller/update_company.html', context)


def company_update_redirect(request, pk):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = Company.objects.filter(pk=pk).first()
            company.name = form.cleaned_data['name']
            company.number_of_randoms = form.cleaned_data['number_of_randoms']
            company.number_of_alternates = form.cleaned_data['number_of_alternates']
            company.save()
            return redirect('RandomPuller:company_employees', pk=company.pk)
    return redirect('RandomPuller:update_company', pk=pk)


def pull_randoms(request, pk):
    company = Company.objects.filter(pk=pk).first()
    employee_pk_list = Employee.objects.all().values_list('pk', flat=True)
    try:
        random_sample = random.sample(list(employee_pk_list), company.get_total_pulls())
    except ValueError:
        pass
    employees = list(Employee.objects.filter(pk__in=random_sample))
    pulled_randoms_object = PulledRandoms.objects.create()

    for _ in range(company.number_of_randoms):
        pulled_randoms_object.pulled_randoms.add(employees.pop(0))

    for _ in range(company.number_of_alternates):
        pulled_randoms_object.pulled_alternates.add(employees.pop(0))

    return redirect('RandomPuller:pulled_randoms', id=pulled_randoms_object.id, pk=pk)


def pulled_randoms(request, pk, id):
    company = Company.objects.filter(pk=pk).first()
    pulled = PulledRandoms.objects.filter(id=id).first()
    date_time_pulled = pulled.date_pulled
    random_employees = pulled.pulled_randoms.all()
    alternate_employees = pulled.pulled_alternates.all()

    context = {
        'company': company,
        'pulled_date': date_time_pulled,
        'pulled_randoms': random_employees,
        'pulled_alternates': alternate_employees,
    }
    return render(request, 'RandomPuller/pulled_randoms.html', context)

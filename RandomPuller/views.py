from django.shortcuts import render, redirect

import random

from .models import Company, Employee
from .forms import CompanyForm, EmployeeForm


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
            return redirect('RandomPuller:company_employees', name_of_company=company.name.replace(' ', '_'))
    return redirect('RandomPuller:new_employee')


def delete_employee(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    company = Company.objects.filter(pk=employee.company.pk).first()
    Employee.objects.filter(pk=pk).delete()
    return redirect('RandomPuller:company_employees', name_of_company=company.name.replace(' ', '_'))

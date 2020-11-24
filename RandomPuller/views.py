from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import FileResponse

import io
import random

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from .forms import CompanyForm, EmployeeForm
from .models import Company, Employee, PulledRandoms

from EliteConsortiumWebSite.settings import TIME_ZONE


# Create your views here.
@login_required()
def index(request):
    companies = Company.objects.all()

    context = {
        'companies': companies,
    }
    return render(request, 'RandomPuller/index.html', context)


@login_required()
def company_employees(request, pk):
    company = Company.objects.filter(pk=pk).first()
    employees = Employee.objects.filter(company=company)

    context = {
        'company': company,
        'employees': employees,
    }
    return render(request, 'RandomPuller/company_employees.html', context)


@login_required()
def new_company(request):
    c_form = CompanyForm
    context = {
        'form': c_form,
    }
    return render(request, 'RandomPuller/add_company.html', context)


@login_required()
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


@login_required()
def delete_company(request, pk):
    Company.objects.filter(pk=pk).delete()
    return redirect('RandomPuller:index')


@login_required()
def new_employee(request, pk):
    company = Company.objects.filter(pk=pk).first()
    e_form = EmployeeForm
    context = {
        'company': company,
        'form': e_form,
    }
    return render(request, 'RandomPuller/add_employee.html', context)


@login_required()
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
    return redirect('RandomPuller:new_employee', pk=pk)


@login_required()
def delete_employee(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    company = Company.objects.filter(pk=employee.company.pk).first()
    Employee.objects.filter(pk=pk).delete()
    return redirect('RandomPuller:company_employees', pk=company.pk)


@login_required()
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


@login_required()
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


@login_required()
def pull_randoms(request, pk):
    company = Company.objects.filter(pk=pk).first()
    employee_pk_list = Employee.objects.filter(company=company).values_list('pk', flat=True)
    try:
        random_sample = random.sample(list(employee_pk_list), company.get_total_pulls())
    except ValueError:
        return redirect('RandomPuller:company_employees', pk=pk)

    employees = list(Employee.objects.filter(pk__in=random_sample))
    pulled_randoms_object = PulledRandoms.objects.create(pulled_company=company)

    for _ in range(company.number_of_randoms):
        pulled_randoms_object.pulled_randoms.add(employees.pop(0))

    for _ in range(company.number_of_alternates):
        pulled_randoms_object.pulled_alternates.add(employees.pop(0))

    return redirect('RandomPuller:pulled_randoms', id=pulled_randoms_object.id, pk=pk)


@login_required()
def pulled_randoms(request, pk, id):
    company = Company.objects.filter(pk=pk).first()
    pulled = PulledRandoms.objects.filter(id=id).first()
    date_time_pulled = pulled.date_pulled
    random_employees = pulled.pulled_randoms.all()
    alternate_employees = pulled.pulled_alternates.all()

    context = {
        'company': company,
        'pulled': pulled,
        'pulled_date': date_time_pulled,
        'pulled_randoms': random_employees,
        'pulled_alternates': alternate_employees,
    }
    return render(request, 'RandomPuller/pulled_randoms.html', context)


def all_pulled(request):
    all_pulled_randoms = PulledRandoms.objects.all()

    context = {
        'pulled_list': all_pulled_randoms
    }
    return render(request, 'RandomPuller/all_pulled.html', context)


@login_required()
def download_pdf(request, id):
    pulled_list = PulledRandoms.objects.filter(id=id).first()
    pulled_rands = pulled_list.pulled_randoms.all()
    pulled_alts = pulled_list.pulled_alternates.all()

    pdf_buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        pdf_buffer,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
        pagesize=letter
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    date_pulled = pulled_list.get_local_date()
    time_pulled = pulled_list.get_local_time()

    elements = [Paragraph(f'Pulled Randoms for {pulled_list.pulled_company.name}', styles['Heading1']),
                Paragraph(
                    f'Pulled on: {date_pulled} at {time_pulled}',
                    styles['Heading2']),
                Paragraph(f'Randoms:', styles['Heading3'])]
    for count, rand in enumerate(pulled_rands, start=1):
        elements.append(Paragraph(f'{count}: {rand.last_name}, {rand.first_name}', styles['Justify']))

    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f'Alternates:', styles['Heading3']))
    for count, alt in enumerate(pulled_alts, start=1):
        elements.append(Paragraph(f'{count}: {alt.last_name}, {alt.first_name}', styles['Justify']))

    doc.build(elements)

    pdf_buffer.seek(0)

    file_prepared_company_name = f'{"_".join(pulled_list.pulled_company.name.split(" "))}'
    date_format = '%b-%d-%Y'
    file_prepared_date_time = f'{":".join(str(pulled_list.date_pulled.date().strftime(date_format)).split(" "))}'
    file_name = f'{file_prepared_company_name}-{file_prepared_date_time}.pdf'

    return FileResponse(pdf_buffer, as_attachment=True, filename=file_name)

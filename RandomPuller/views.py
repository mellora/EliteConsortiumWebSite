from django.shortcuts import render

from .models import Company, Employee


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

from django.shortcuts import render

from .models import Company


# Create your views here.
def index(request):
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'RandomPuller/index.html', context)

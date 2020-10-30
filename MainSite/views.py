from django.shortcuts import render
from.models import Pricing


# Create your views here.
def index(request):
    return render(request, 'MainSite/index.html')


def who_needs_a_consortium(request):
    return render(request, 'MainSite/who_needs_a_consortium.html')


def what_can_elite_do_for_you(request):
    return render(request, 'MainSite/what_can_elite_do_for_you.html')


def pricing(request):
    prices = Pricing.objects.all()
    return render(request, 'MainSite/pricing.html', {'prices': prices})


def did_you_know_dot_requires(request):
    return render(request, 'MainSite/did_you_know_dot_requires.html')


def contact_us(request):
    return render(request, 'MainSite/contact_us.html')

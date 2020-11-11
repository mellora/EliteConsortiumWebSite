from django.shortcuts import render

from .models import NonMemberConsortiumPricing, MemberConsortiumPricing, ThirdPartyProgramSupportFees


# Create your views here.
def index(request):
    return render(request, 'MainSite/index.html')


def who_needs_a_consortium(request):
    return render(request, 'MainSite/who_needs_a_consortium.html')


def what_can_elite_do_for_you(request):
    return render(request, 'MainSite/what_can_elite_do_for_you.html')


def pricing(request):
    non_member_prices = NonMemberConsortiumPricing.objects.all()
    member_prices = MemberConsortiumPricing.objects.all()
    third_party_fees = ThirdPartyProgramSupportFees.objects.all()
    context = {
        'non_member': non_member_prices,
        'member': member_prices,
        'third_party': third_party_fees
    }
    return render(request, 'MainSite/pricing.html', context)


def did_you_know_dot_requires(request):
    return render(request, 'MainSite/did_you_know_dot_requires.html')


def contact_us(request):
    return render(request, 'MainSite/contact_us.html')

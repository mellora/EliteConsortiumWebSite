from django.contrib import admin

from .models import NonMemberConsortiumPricing, MemberConsortiumPricing, ThirdPartyProgramSupportFees


# Modify Model view
class NonMemberConsortiumPricingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['service_name']}),
        ('Pricing Info', {'fields': ['price', 'extra_cost_text', 'extra_cost']})
    ]


class MemberConsortiumPricingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['service_name']}),
        ('Pricing Info (If there is no min and max price difference, input the price into both)',
         {'fields': ['min_price', 'max_price', 'extra_cost_text', 'extra_cost']})
    ]


# Register your models here.
admin.site.register(NonMemberConsortiumPricing, NonMemberConsortiumPricingAdmin)
admin.site.register(MemberConsortiumPricing, MemberConsortiumPricingAdmin)
admin.site.register(ThirdPartyProgramSupportFees)

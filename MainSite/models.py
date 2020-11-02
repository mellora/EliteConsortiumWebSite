from django.db import models


# Create your models here.
MAX_DIGIT_SIZE = 5


class NonMemberConsortiumPricing(models.Model):
    service_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=MAX_DIGIT_SIZE, decimal_places=2, default=0)
    extra_cost = models.DecimalField(max_digits=MAX_DIGIT_SIZE, decimal_places=2, default=0)

    class Meta:
        app_label = 'MainSite'
        verbose_name = 'Non Member Consortium Pricing'
        verbose_name_plural = 'Non Member Consortium Pricing'

    def __str__(self):
        return self.service_name


class MemberConsortiumPricing(models.Model):
    service_name = models.CharField(max_length=200)
    min_price = models.DecimalField(max_digits=MAX_DIGIT_SIZE, decimal_places=2, default=0)
    max_price = models.DecimalField(max_digits=MAX_DIGIT_SIZE, decimal_places=2, default=0)
    extra_cost = models.DecimalField(max_digits=MAX_DIGIT_SIZE, decimal_places=2, default=0)

    class Meta:
        app_label = 'MainSite'
        verbose_name = 'Member Consortium Pricing'
        verbose_name_plural = 'Member Consortium Pricing'

    def __str__(self):
        return self.service_name\


from django.db import models
from django.core.validators import MinValueValidator

from django.utils import timezone

import uuid


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    number_of_randoms = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0)])
    number_of_alternates = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0)])

    class Meta:
        app_label = 'RandomPuller'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_total_pulls(self):
        return self.number_of_randoms + self.number_of_alternates


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        app_label = 'RandomPuller'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['last_name', 'first_name']
        unique_together = ['first_name', 'last_name', 'company']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class PulledRandoms(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    date_pulled = models.DateTimeField(auto_now_add=True)
    pulled_company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    pulled_randoms = models.ManyToManyField(Employee, related_name='pulled_randoms_list')
    pulled_alternates = models.ManyToManyField(Employee, related_name='pulled_alternates_list')

    class Meta:
        app_label = 'RandomPuller'
        verbose_name = 'Pulled Random List'
        verbose_name_plural = 'Pulled Random Lists'
        ordering = ['pulled_company', 'date_pulled']

    def __str__(self):
        return f'{self.pulled_company.name}: {self.date_pulled}'

    def get_local_date(self, date_format='%b %d, %Y'):
        return timezone.localtime(self.date_pulled).date().strftime(date_format)

    def get_local_time(self, time_format='%I:%M %p'):
        return timezone.localtime(self.date_pulled).time().strftime(time_format)

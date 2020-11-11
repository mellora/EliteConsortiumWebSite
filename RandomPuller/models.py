from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    number_of_randoms = models.IntegerField(null=True, blank=True)
    number_of_alternates = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'RandomPuller'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']

    def __str__(self):
        return self.name


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

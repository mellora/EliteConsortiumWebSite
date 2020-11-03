from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    number_of_randoms = models.IntegerField(null=True, blank=True)
    number_of_alternates = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

from django import forms
from django.forms import ModelForm

from .models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'number_of_randoms', 'number_of_alternates']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'number_of_randoms': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'number_of_alternates': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse

from RandomPuller.models import Company, Employee, PulledRandoms


class TemplateTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('tester1', 'tester1@test.com', 'testerpass')
        self.client.login(username='tester1', password='testerpass')

        self.company = Company.objects.create(name='Test Company')
        self.employee = Employee.objects.create(first_name='Employee 1', last_name='Tester', company=self.company)
        self.pulled = PulledRandoms.objects.create()

    def test_index_template(self):
        response = self.client.get(reverse('RandomPuller:index'))
        self.assertTemplateUsed(response, template_name='RandomPuller/index.html')

    def test_company_employees_template(self):
        response = self.client.get(reverse('RandomPuller:company_employees', args=[self.company.pk]))
        self.assertTemplateUsed(response, template_name='RandomPuller/company_employees.html')

    def test_new_company_template(self):
        response = self.client.get(reverse('RandomPuller:new_company'))
        self.assertTemplateUsed(response, template_name='RandomPuller/add_company.html')

    def test_new_employee_template(self):
        response = self.client.get(reverse('RandomPuller:new_employee', args=[self.company.pk]))
        self.assertTemplateUsed(response, template_name='RandomPuller/add_employee.html')

    def test_update_company_template(self):
        response = self.client.get(reverse('RandomPuller:update_company', args=[self.company.pk]))
        self.assertTemplateUsed(response, template_name='RandomPuller/update_company.html')

    def test_pulled_randoms_template(self):
        response = self.client.get(reverse('RandomPuller:pulled_randoms', args=[self.company.pk, self.pulled.id]))
        self.assertTemplateUsed(response, template_name='RandomPuller/pulled_randoms.html')

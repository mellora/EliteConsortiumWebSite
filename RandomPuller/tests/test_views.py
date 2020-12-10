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
        self.pulled = PulledRandoms.objects.create(pulled_company=self.company)

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
    
    def test_all_pulled(self):
        response = self.client.get(reverse('RandomPuller:all_pulled'))
        self.assertTemplateUsed(response, template_name='RandomPuller/all_pulled.html')


class RedirectTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('tester1', 'tester1@test.com', 'testerpass')
        self.client.login(username='tester1', password='testerpass')

    def test_add_company_get_redirect(self):
        response = self.client.get(reverse('RandomPuller:add_company'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:new_company'))

    def test_add_company_post_redirect(self):
        data = {
            'name': 'Test Company',
            'number_of_randoms': 4,
            'number_of_alternates': 2
        }
        response = self.client.post(reverse('RandomPuller:add_company'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:index'))

    def test_delete_company_redirect(self):
        company = Company.objects.create(
            name="Test Company",
            number_of_randoms=2,
            number_of_alternates=1
        )
        response = self.client.post(reverse('RandomPuller:delete_company', args=[company.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:index'))

    def test_add_employee_get_redirect(self):
        company = Company.objects.create(
            name="Test Company",
            number_of_randoms=2,
            number_of_alternates=1
        )
        response = self.client.get(reverse('RandomPuller:add_employee', args=[company.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:new_employee', args=[company.pk]))

    def test_add_employee_post_redirect(self):
        data = {
            'first_name': 'Test',
            'last_name': 'Employee'
        }
        company = Company.objects.create(
            name="Test Company",
            number_of_randoms=2,
            number_of_alternates=1
        )
        response = self.client.post(reverse('RandomPuller:add_employee', args=[company.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:company_employees', args=[company.pk]))

    def test_delete_employee_redirect(self):
        company = Company.objects.create(
            name="Test Company",
            number_of_randoms=2,
            number_of_alternates=1
        )
        employee = Employee.objects.create(
            first_name='Test',
            last_name='Employee',
            company=company
        )
        response = self.client.get(reverse('RandomPuller:delete_employee', args=[employee.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:company_employees', args=[company.pk]))

    def test_company_update_get_redirect(self):
        company = Company.objects.create(
            name="Test Company",
            number_of_randoms=2,
            number_of_alternates=1
        )
        response = self.client.get(reverse('RandomPuller:company_update_redirect', args=[company.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:update_company', args=[company.pk]))

    def test_company_update_post_redirect(self):
        company = Company.objects.create(
            name="Test Company",
            number_of_randoms=2,
            number_of_alternates=1
        )
        data = {
            'name': 'Test Company',
            'number_of_randoms': 4,
            'number_of_alternates': 2
        }
        response = self.client.post(reverse('RandomPuller:company_update_redirect', args=[company.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:company_employees', args=[company.pk]))

    def test_pull_randoms_valid_redirect(self):
        company = Company.objects.create(
            name="Test Company",
            number_of_randoms=2,
            number_of_alternates=1
        )
        Employee.objects.create(first_name="Employee", last_name=1, company=company)
        Employee.objects.create(first_name="Employee", last_name=2, company=company)
        Employee.objects.create(first_name="Employee", last_name=3, company=company)
        Employee.objects.create(first_name="Employee", last_name=4, company=company)
        response = self.client.get(reverse('RandomPuller:pull_randoms', args=[company.pk]))
        test_pulled_list = PulledRandoms.objects.all().first()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:pulled_randoms', args=[company.pk, test_pulled_list.id]))

    def test_pull_randoms_invalid_redirect(self):
        company = Company.objects.create(
            name="Test Company",
            number_of_randoms=2,
            number_of_alternates=1
        )
        response = self.client.get(reverse('RandomPuller:pull_randoms', args=[company.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('RandomPuller:company_employees', args=[company.pk]))

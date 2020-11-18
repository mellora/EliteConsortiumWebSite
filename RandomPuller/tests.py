from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Company, Employee, PulledRandoms


# Create your tests here.
class CompanyModelTest(TestCase):

    def test_save_and_retrieving_new_companies(self):
        new_company_1 = Company(name='Elite Consortium')
        new_company_1.save()

        new_company_2 = Company(name='Kind Properties')
        new_company_2.save()
        
        saved_companies = Company.objects.all()
        self.assertEqual(saved_companies.count(), 2)

        first_saved_company = saved_companies[0]
        self.assertEqual(first_saved_company, new_company_1)

        second_saved_company = saved_companies[1]
        self.assertEqual(second_saved_company, new_company_2)

    def test_save_and_retrieving_new_companies_with_params(self):
        new_company_1 = Company(name='Elite Consortium', number_of_randoms=2)
        new_company_1.save()

        new_company_2 = Company(name='Kind Properties', number_of_randoms=5, number_of_alternates=2)
        new_company_2.save()

        saved_companies = Company.objects.all()
        self.assertEqual(saved_companies.count(), 2)

        first_saved_company = saved_companies[0]
        self.assertEqual(first_saved_company, new_company_1)
        self.assertEqual(first_saved_company.number_of_randoms, new_company_1.number_of_randoms)
        self.assertEqual(first_saved_company.number_of_alternates, new_company_1.number_of_alternates)

        second_saved_company = saved_companies[1]
        self.assertEqual(second_saved_company, new_company_2)
        self.assertEqual(second_saved_company.number_of_randoms, new_company_2.number_of_randoms)
        self.assertEqual(second_saved_company.number_of_alternates, new_company_2.number_of_alternates)

    def test_delete_company(self):
        new_company_1 = Company(name='Elite Consortium', number_of_randoms=2)
        new_company_1.save()

        new_company_2 = Company(name='Kind Properties', number_of_randoms=5, number_of_alternates=2)
        new_company_2.save()

        saved_companies = Company.objects.all()
        self.assertEqual(saved_companies.count(), 2)

        Company.objects.filter(name='Elite Consortium').delete()
        saved_companies = Company.objects.all()
        self.assertEqual(saved_companies.count(), 1)

    def test_correct_total_pull_number_returned(self):
        new_company_1 = Company.objects.create(name='Test Company 1', number_of_randoms=2)
        new_company_2 = Company.objects.create(name='Test Company 2', number_of_randoms=2, number_of_alternates=1)
        new_company_3 = Company.objects.create(name='Test Company 3', number_of_randoms=4, number_of_alternates=2)

        saved_company_1 = Company.objects.filter(pk=new_company_1.pk).first()
        saved_company_2 = Company.objects.filter(pk=new_company_2.pk).first()
        saved_company_3 = Company.objects.filter(pk=new_company_3.pk).first()

        self.assertIs(saved_company_1.get_total_pulls(), 2)
        self.assertIs(saved_company_2.get_total_pulls(), 3)
        self.assertIs(saved_company_3.get_total_pulls(), 6)


class EmployeeModelTest(TestCase):

    def test_save_and_retrieving_new_employees(self):
        test_company = Company(name='Test Company')
        test_company.save()

        new_employee_1 = Employee(first_name='Employee', last_name='1', company=test_company)
        new_employee_1.save()
        new_employee_2 = Employee(first_name='Employee', last_name='2', company=test_company)
        new_employee_2.save()
        new_employee_3 = Employee(first_name='Employee', last_name='3', company=test_company)
        new_employee_3.save()
        new_employee_4 = Employee(first_name='Employee', last_name='4', company=test_company)
        new_employee_4.save()
        new_employee_5 = Employee(first_name='Employee', last_name='5', company=test_company)
        new_employee_5.save()

        all_employees = Employee.objects.all()
        self.assertEqual(all_employees.count(), 5)

        self.assertEqual(new_employee_1, all_employees[0])
        self.assertEqual(new_employee_2, all_employees[1])
        self.assertEqual(new_employee_3, all_employees[2])
        self.assertEqual(new_employee_4, all_employees[3])
        self.assertEqual(new_employee_5, all_employees[4])
    
    def test_delete_employees(self):
        new_company_1 = Company(name='Elite Consortium', number_of_randoms=2)
        new_company_1.save()

        new_company_2 = Company(name='Kind Properties', number_of_randoms=5, number_of_alternates=2)
        new_company_2.save()

        new_employee_1 = Employee(first_name='Employee', last_name='1', company=new_company_1)
        new_employee_1.save()
        new_employee_2 = Employee(first_name='Employee', last_name='2', company=new_company_2)
        new_employee_2.save()
        new_employee_3 = Employee(first_name='Employee', last_name='3', company=new_company_1)
        new_employee_3.save()
        new_employee_4 = Employee(first_name='Employee', last_name='4', company=new_company_2)
        new_employee_4.save()
        new_employee_5 = Employee(first_name='Employee', last_name='5', company=new_company_1)
        new_employee_5.save()
        
        employee_list = Employee.objects.all()
        self.assertEqual(employee_list.count(), 5)

        user_to_delete = Employee.objects.filter(first_name='Employee', last_name='3').first()
        Employee.objects.filter(pk=user_to_delete.pk).delete()

        employee_list = Employee.objects.all()
        self.assertEqual(employee_list.count(), 4)


class CompanyAndEmployeeModelTest(TestCase):

    def test_employee_pull_from_company(self):
        new_company_1 = Company(name='Elite Consortium', number_of_randoms=2)
        new_company_1.save()

        new_company_2 = Company(name='Kind Properties', number_of_randoms=5, number_of_alternates=2)
        new_company_2.save()

        new_employee_1 = Employee(first_name='Employee', last_name='1', company=new_company_1)
        new_employee_1.save()
        new_employee_2 = Employee(first_name='Employee', last_name='2', company=new_company_1)
        new_employee_2.save()
        new_employee_3 = Employee(first_name='Employee', last_name='3', company=new_company_2)
        new_employee_3.save()
        new_employee_4 = Employee(first_name='Employee', last_name='4', company=new_company_1)
        new_employee_4.save()
        new_employee_5 = Employee(first_name='Employee', last_name='5', company=new_company_2)
        new_employee_5.save()

        employee_list_1 = Employee.objects.filter(company__name='Elite Consortium')
        self.assertEqual(employee_list_1.count(), 3)

        employee_list_2 = Employee.objects.filter(company__name='Kind Properties')
        self.assertEqual(employee_list_2.count(), 2)

        self.assertEqual(employee_list_1[0].company, new_company_1)
        self.assertEqual(employee_list_1[1].company, new_company_1)
        self.assertEqual(employee_list_1[2].company, new_company_1)
        self.assertEqual(employee_list_2[0].company, new_company_2)
        self.assertEqual(employee_list_2[1].company, new_company_2)


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

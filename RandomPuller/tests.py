from django.test import TestCase

from .models import Company, Employee


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


class EmployeeModelTest(TestCase):

    def test_save_and_retrieving_new_employees(self):
        test_company = Company(name='Test Company')
        test_company.save()

        new_employee_1 = Employee(first_name='Employee', last_name='1', company_name=test_company)
        new_employee_1.save()
        new_employee_2 = Employee(first_name='Employee', last_name='2', company_name=test_company)
        new_employee_2.save()
        new_employee_3 = Employee(first_name='Employee', last_name='3', company_name=test_company)
        new_employee_3.save()
        new_employee_4 = Employee(first_name='Employee', last_name='4', company_name=test_company)
        new_employee_4.save()
        new_employee_5 = Employee(first_name='Employee', last_name='5', company_name=test_company)
        new_employee_5.save()

        all_employees = Employee.objects.all()
        self.assertEqual(all_employees.count(), 5)

        self.assertEqual(new_employee_1, all_employees[0])
        self.assertEqual(new_employee_2, all_employees[1])
        self.assertEqual(new_employee_3, all_employees[2])
        self.assertEqual(new_employee_4, all_employees[3])
        self.assertEqual(new_employee_5, all_employees[4])


class CompanyAndEmployeeModelTest(TestCase):

    def test_employee_pull_from_company(self):
        new_company_1 = Company(name='Elite Consortium', number_of_randoms=2)
        new_company_1.save()

        new_company_2 = Company(name='Kind Properties', number_of_randoms=5, number_of_alternates=2)
        new_company_2.save()

        new_employee_1 = Employee(first_name='Employee', last_name='1', company_name=new_company_1)
        new_employee_1.save()
        new_employee_2 = Employee(first_name='Employee', last_name='2', company_name=new_company_1)
        new_employee_2.save()
        new_employee_3 = Employee(first_name='Employee', last_name='3', company_name=new_company_2)
        new_employee_3.save()
        new_employee_4 = Employee(first_name='Employee', last_name='4', company_name=new_company_1)
        new_employee_4.save()
        new_employee_5 = Employee(first_name='Employee', last_name='5', company_name=new_company_2)
        new_employee_5.save()

        employee_list_1 = Employee.objects.filter(company_name__name='Elite Consortium')
        self.assertEqual(employee_list_1.count(), 3)

        employee_list_2 = Employee.objects.filter(company_name__name='Kind Properties')
        self.assertEqual(employee_list_2.count(), 2)

        self.assertEqual(employee_list_1[0].company_name, new_company_1)
        self.assertEqual(employee_list_1[1].company_name, new_company_1)
        self.assertEqual(employee_list_1[2].company_name, new_company_1)
        self.assertEqual(employee_list_2[0].company_name, new_company_2)
        self.assertEqual(employee_list_2[1].company_name, new_company_2)
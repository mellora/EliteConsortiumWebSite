from django.test import TestCase

from RandomPuller.models import Company, Employee, PulledRandoms


class CompanyTests(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name='Test Company',
            number_of_randoms=2,
            number_of_alternates=1
        )
    
    def test_to_str(self):
        self.assertEqual(self.company.name, self.company.__str__())
    
    def test_get_total_pulls(self):
        self.assertEqual(
            self.company.get_total_pulls(),
            self.company.number_of_randoms + self.company.number_of_alternates
        )


class EmployeeTests(TestCase):

    def setUp(self):
        company = Company.objects.create(
            name='Test Company',
            number_of_randoms=2,
            number_of_alternates=1
        )
        self.employee = Employee.objects.create(
            first_name="Test",
            last_name='Employee',
            company=company
        )

    def test_to_str(self):
        self.assertEqual(
            f'{self.employee.last_name}, {self.employee.first_name}',
            self.employee.__str__()
        )

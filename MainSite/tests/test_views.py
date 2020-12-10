from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User

from MainSite.forms import UserLoginForm


class TemplateTests(TestCase):

    def test_index_template(self):
        response = self.client.get(reverse('MainSite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MainSite/index.html')

    def test_who_needs_a_consortium_template(self):
        response = self.client.get(reverse('MainSite:who_needs_a_consortium'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MainSite/who_needs_a_consortium.html')

    def test_what_can_elite_do_for_you_template(self):
        response = self.client.get(reverse('MainSite:what_can_elite_do_for_you'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MainSite/what_can_elite_do_for_you.html')

    def test_pricing_template(self):
        response = self.client.get(reverse('MainSite:pricing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MainSite/pricing.html')

    def test_did_you_know_dot_requires_template(self):
        response = self.client.get(reverse('MainSite:did_you_know_dot_requires'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MainSite/did_you_know_dot_requires.html')

    def test_contact_us_template(self):
        response = self.client.get(reverse('MainSite:contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MainSite/contact_us.html')

    def test_login_template(self):
        response = self.client.get(reverse('MainSite:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MainSite/login.html')


class LoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('tester1', 'tester1@test.com', 'testerpass')
        self.credentials = {
            'username': 'tester1',
            'password': 'testerpass',
        }

    def test_login_request_post(self):
        response = self.client.post(reverse('MainSite:login'), self.credentials)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('MainSite:index'))

    def test_login_request_get(self):
        response = self.client.get(reverse('MainSite:login'))
        self.assertEqual(response.status_code, 200)


class LogoutTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('tester1', 'tester1@test.com', 'testerpass')
        self.client.login(username='tester1', password='testerpass')

    def test_logout_request(self):
        response = self.client.get(reverse('MainSite:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('MainSite:index'))

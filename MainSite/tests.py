from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TemplateTests(TestCase):

    def test_index(self):
        response = self.client.get(reverse('MainSite:index'))
        self.assertTemplateUsed(response, 'MainSite/index.html')

    def test_who_needs_a_consortium(self):
        response = self.client.get(reverse('MainSite:who_needs_a_consortium'))
        self.assertTemplateUsed(response, 'MainSite/who_needs_a_consortium.html')

    def test_what_can_elite_do_for_you(self):
        response = self.client.get(reverse('MainSite:what_can_elite_do_for_you'))
        self.assertTemplateUsed(response, 'MainSite/what_can_elite_do_for_you.html')

    def test_pricing(self):
        response = self.client.get(reverse('MainSite:pricing'))
        self.assertTemplateUsed(response, 'MainSite/pricing.html')

    def test_did_you_know_dot_requires(self):
        response = self.client.get(reverse('MainSite:did_you_know_dot_requires'))
        self.assertTemplateUsed(response, 'MainSite/did_you_know_dot_requires.html')

    def test_contact_us(self):
        response = self.client.get(reverse('MainSite:contact_us'))
        self.assertTemplateUsed(response, 'MainSite/contact_us.html')
        
    def test_login_template(self):
        response = self.client.get(reverse('MainSite:login'))
        self.assertTemplateUsed(response, 'MainSite/login.html')

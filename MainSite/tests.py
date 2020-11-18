from django.test import TestCase


# Create your tests here.
class TemplateTests(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'MainSite/index.html')

    def test_who_needs_a_consortium(self):
        response = self.client.get('/who-needs-a-consortium/')
        self.assertTemplateUsed(response, 'MainSite/who_needs_a_consortium.html')

    def test_what_can_elite_do_for_you(self):
        response = self.client.get('/what-can-elite-do-for-you/')
        self.assertTemplateUsed(response, 'MainSite/what_can_elite_do_for_you.html')

    def test_pricing(self):
        response = self.client.get('/pricing/')
        self.assertTemplateUsed(response, 'MainSite/pricing.html')

    def test_did_you_know_dot_requires(self):
        response = self.client.get('/did-you-know-dot-requires/')
        self.assertTemplateUsed(response, 'MainSite/did_you_know_dot_requires.html')

    def test_contact_us(self):
        response = self.client.get('/contact-us/')
        self.assertTemplateUsed(response, 'MainSite/contact_us.html')

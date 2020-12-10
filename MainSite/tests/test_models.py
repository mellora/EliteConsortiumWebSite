from django.test import TestCase
from django.urls import reverse

from MainSite.models import NonMemberConsortiumPricing, MemberConsortiumPricing, ThirdPartyProgramSupportFees


class NonMemberConsortiumPricingTests(TestCase):

    def setUp(self):
        self.non_member = NonMemberConsortiumPricing.objects.create(
            service_name='Test Non Member Price',
            price=25.00,
            extra_cost_text='Extra Cost',
            extra_cost=5.25
        )

    def test_to_str(self):
        self.assertEqual(self.non_member.__str__(), self.non_member.service_name)


class MemberConsortiumPricingTests(TestCase):

    def setUp(self):
        self.member = MemberConsortiumPricing.objects.create(
            service_name='Test Member Price',
            min_price=50.25,
            max_price=50.25,
            extra_cost_text='Extra Cost',
            extra_cost=2.50
        )

    def test_to_str(self):
        self.assertEqual(self.member.__str__(), self.member.service_name)


class ThirdPartyProgramSupportFeesTests(TestCase):

    def setUp(self):
        self.third_party = ThirdPartyProgramSupportFees.objects.create(
            service='Test Third Party',
            charge_rate='By annually',
            driver_num='25-80',
            price=99.99
        )

    def test_to_str(self):
        self.assertEqual(self.third_party.__str__(), self.third_party.service)

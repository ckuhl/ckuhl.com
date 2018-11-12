from django import test
from django.urls import reverse


class TestCoreViews(test.TestCase):
    """Bare minimum testing, used to ensure that everything is working fine"""

    def test_home_page_loads(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_loads(self):
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)

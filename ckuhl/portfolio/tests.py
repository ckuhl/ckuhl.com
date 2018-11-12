from django import test
from django.urls import reverse


class PortfolioViewsTest(test.TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)

    # TODO: Test rest of Portfolio views

from django import test
from django.urls import reverse


class BlogViewsTest(test.TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)

    def test_archive_loads(self):
        response = self.client.get(reverse('blog:archive'))
        self.assertEqual(response.status_code, 200)

    def test_old_index_redirects(self):
        response = self.client.get(reverse('blog:old_archive'), follow=True)
        self.assertRedirects(response,
                             reverse('blog:archive'),
                             status_code=301)

    # TODO: Test rest of blog views

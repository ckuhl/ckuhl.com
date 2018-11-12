from django import test
from django.urls import reverse


class TestShortlinkViews(test.TestCase):
    """Bare minimum testing, used to ensure that everything is working fine"""

    def test_base_url_redirects_home(self):
        response = self.client.get(reverse('shortlink:root'),
                                   follow=True)

        self.assertRedirects(response,
                             reverse('core:home'),
                             status_code=301)

    def test_image_block_redirect(self):
        """
        Since this path depends on DB data being loaded, only test that
        the redirect is properly generated
        """
        response = self.client.get(reverse('shortlink:image-block-x'))
        self.assertEquals(response['location'],
                          reverse('portfolio:project',
                                  args=['image-block-x']))

    def test_mips_vm_redirect(self):
        """
        Since this path depends on DB data being loaded, only test that
        the redirect is properly generated
        """
        response = self.client.get(reverse('shortlink:mips-vm'))

        self.assertEquals(response['location'],
                          reverse('portfolio:project',
                                  args=['mips-vm']))

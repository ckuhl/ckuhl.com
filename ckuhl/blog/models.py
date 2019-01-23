from django.urls import reverse

from _commons.models.page import Page


class BlogPost(Page):
    class Meta:
        app_label = 'blog'

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.url])

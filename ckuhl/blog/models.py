from typing import Optional

from django.urls import reverse

from _commons.models import page


class BlogPost(page.Page):
    class Meta:
        app_label = 'blog'

    def get_absolute_url(self) -> Optional[str]:
        return reverse('blog:post', args=[self.url])

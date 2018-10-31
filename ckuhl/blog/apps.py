from django.apps import AppConfig

from _commons.flat_page_loader import load_pages


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        load_pages(self, 'BlogPost')

from django.apps import AppConfig

from _commons.flat_page_loader import load_pages


class PortfolioConfig(AppConfig):
    name = 'portfolio'

    def ready(self):
        load_pages(self, 'PortfolioProject')

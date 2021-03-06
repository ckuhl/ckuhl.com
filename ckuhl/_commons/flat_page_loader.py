import logging

from django.apps import AppConfig
from django.conf import settings
from django.db import OperationalError, models

from _commons.flat_page import FlatPage


def load_pages(app_config: AppConfig,
               model_name: str) -> None:
    """
    Load all flatpages for a given model into the database
    :param app_config: the AppConfig we're loading a model from
    :param model_name: the name of the model, since you can't import from here
    """
    log = logging.getLogger(__name__)

    # typing added to get IDE autocompletion
    # we load the model this way to avoid circular imports
    model: models.Model = app_config.get_model(model_name)

    flatpage_root = settings.RESOURCEFILES_DIR / app_config.name / 'flatpages'
    page_count = 0
    for page in flatpage_root.rglob('*.md'):
        page_count += 1

        f = FlatPage(page, flatpage_root)
        try:
            model(
                date=f.date,
                updated=f.meta.get('updated'),
                published=f['published'],
                file_path=f.file,
                url=f.url,
                body=f.body,
                category=f['category'],
                title=f['title'],
            ).save()

        except OperationalError:
            log.error(f'The table {model} does not exist!')
            log.error(f'Skipping loading pages...')
            return

    log.info(f'{page_count} {model_name} pages loaded')

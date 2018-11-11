from django.conf import settings
from django.db import models


class Page(models.Model):
    """Representation of the FlatPage textfile"""

    class Meta:
        abstract = True
        app_label = 'core'

    # file path fields
    # While other fields _should_ be unique, the file path is guaranteed to
    file_path = models.FilePathField(
        # Must stringify our Path because Django 2.1 can't serialize it
        path=str(settings.RESOURCEFILES_DIR / Meta.app_label / 'flatpages'),
        match='*.md',
        recursive=True,
        primary_key=True,
        unique=True,
        null=False)
    date = models.DateField(null=False)

    updated = models.DateField(null=True)

    published = models.BooleanField(null=False)

    url = models.CharField(max_length=64,
                           unique=True,
                           null=False)

    # metadata fields
    title = models.TextField(null=False,
                             unique=True)
    category = models.TextField(null=False)

    # body fields
    body = models.TextField(null=False)

    # TODO: Eventually include tags (either as a field, or a linked table)

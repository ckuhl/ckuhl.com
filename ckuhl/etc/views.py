from django.shortcuts import render
import yaml
from django.conf import settings


def words_page(request):
    words = yaml.load(
            (settings.RESOURCEFILES_DIR / 'etc' / 'words.yaml').open(),
            Loader=yaml.FullLoader
            )

    return render(
            request,
            'etc/words.html',
            context={'dictionary': words}
            )

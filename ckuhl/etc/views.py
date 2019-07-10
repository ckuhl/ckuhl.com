import yaml
from django.conf import settings
from django.shortcuts import render


def words_page(request):
    """
    Load YAML document of word definitions, and provide it to the template
    """
    words_file = settings.RESOURCEFILES_DIR / 'etc' / 'words.yaml'
    words = yaml.safe_load(words_file.open())
    return render(request, 'etc/words.html', context={'dictionary': words})

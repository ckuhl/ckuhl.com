import yaml
from django.conf import settings
from django.shortcuts import render


def root_page(request):
    """Return the (currently hand-written) root page for this section"""
    return render(request, 'etc/home.html')


def words_page(request):
    """
    Load YAML document of word definitions, and provide it to the template

    TODO: Define some sort of schema for the dictionary file
    """
    words_file = settings.RESOURCEFILES_DIR / 'etc' / 'words.yaml'
    words = yaml.safe_load(words_file.open())
    return render(request, 'etc/words.html', context={'words': words})


def about_page(request):
    """Return the "About me" page"""
    return render(request, 'etc/about.html')


def contact_page(request):
    """Return a page with ways to contact me"""
    return render(request, 'etc/contact.html')

import logging
from pathlib import Path

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import PortfolioProject


log = logging.getLogger(__name__)


def index(request):
    """Listing of my interesting projects"""
    context = {
        'projects': PortfolioProject.objects.values()
            .filter(published=True)
            .order_by('-date'),
    }
    return render(request, 'portfolio/home.html', context=context)


def project(request, project_url):
    """Detail page about a single portfolio project"""
    try:
        fp = PortfolioProject.objects.get(url=project_url, published=True)
    except PortfolioProject.DoesNotExist:
        raise Http404("The project you are looking for does not exist")

    return render(request, 'portfolio/project.html', context={'post': fp})


def project_res(request, project_url, res_url):
    """
    Serve resources belonging to the given project

    TODO: Do this in a less sketchy way -- probably copy / move images on load
    """
    assets: Path = (settings.RESOURCEFILES_DIR
                    / 'portfolio'
                    / 'flatpages'
                    / 'assets')
    image = assets / res_url

    if image.exists():
        return HttpResponse(image.open('rb').read(), content_type="image/png")
    else:
        raise Http404("The file you are looking for does not exist")

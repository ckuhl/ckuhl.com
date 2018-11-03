from django.http import Http404
from django.shortcuts import render

from .models import PortfolioProject


def index(request):
    """Listing of my interesting projects"""
    projects = PortfolioProject.objects.values().order_by('-date')
    return render(request,
                  'portfolio/home.html',
                  context={'projects': projects})


def project(request, project_url):
    """Detail page about a single portfolio project"""
    try:
        fp = PortfolioProject.objects.get(url=project_url)
    except PortfolioProject.DoesNotExist:
        raise Http404("The project you are looking for does not exist")

    return render(request, 'portfolio/project.html', context={'post': fp})

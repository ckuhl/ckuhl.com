from django.shortcuts import render

from blog.models import BlogPost
from portfolio.models import PortfolioProject


def root(request):
    """Render the root page of the site"""
    context = {
        'projects': PortfolioProject.objects.values().order_by('-date')[:3],
        'articles': BlogPost.objects.values().order_by('-date')[:3],
    }
    return render(request, 'core/home.html', context=context)


def contact(request):
    """Information about how to contact me"""
    return render(request, 'core/contact.html')


def about(request):
    """A bio about myself"""
    return render(request, 'core/about.html')

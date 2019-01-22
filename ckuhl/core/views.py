from django.shortcuts import render

from blog.models import BlogPost
from portfolio.models import PortfolioProject


def root(request):
    """Render the root page of the site"""
    context = {
        'portfolio_flatpages': PortfolioProject.objects.values()
                                   .filter(published=True)
                                   .order_by('-date')[:3],
        'blog_flatpages': BlogPost.objects.values()
                              .filter(published=True)
                              .order_by('-date')[:3],
    }
    return render(request, 'core/home.html', context=context)


def contact(request):
    """Information about how to contact me"""
    return render(request, 'core/contact.html')


def about(request):
    """A bio about myself"""
    return render(request, 'core/about.html')

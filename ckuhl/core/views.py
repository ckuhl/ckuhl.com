from django.shortcuts import redirect, render
from django.urls import reverse

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
    return redirect(reverse('etc:contact_singleton'), permanent=True)


def about(request):
    """A bio about myself"""
    return redirect(reverse('etc:about_singleton'), permanent=True)

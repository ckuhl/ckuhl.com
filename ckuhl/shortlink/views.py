from django.shortcuts import redirect
from django.urls import reverse


def root(request):
    """Redirect the root page to the website root"""
    return redirect(reverse('core:home'), permanent=True)


def image_block_x(request):
    """Link to the Image Block X portfolio page (this link is used on GitHub)"""
    return redirect(reverse('portfolio:project', args=['image-block-x']))

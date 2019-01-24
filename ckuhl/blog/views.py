import logging
from pathlib import Path

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render

from blog import models

log = logging.getLogger(__name__)


def root(request):
    """Render the blog home page"""
    context = {
        'flatpages': models.BlogPost.objects.values()
                         .filter(published=True)
                         .order_by('-date')[:10],
    }
    return render(request, 'blog/home.html', context=context)


def archive(request):
    """Render the archive of all pages"""
    # TODO: Limit and paginate blog posts (i.e. 25 or 50 per page?
    context = {
        'flatpages': models.BlogPost.objects.values()
            .filter(published=True)
            .order_by('-date'),
    }
    return render(request, 'blog/archive.html', context=context)


def old_archive(request):
    """Redirect to the new archive URL"""
    return redirect('blog:archive', permanent=True)


def post(request, post_url):
    """Single blog post"""
    try:
        page = models.BlogPost.objects.get(url=post_url, published=True)
    except models.BlogPost.DoesNotExist:
        # TODO: Use local analytics to log this to a DB table
        log.error(f"User tried to get page {post_url} that doesn't exist")
        raise Http404("The blog post you're looking for does not exist")

    try:
        next_post = page.get_next_by_date(published=True)
    except models.BlogPost.DoesNotExist:
        next_post = None

    try:
        prev_post = page.get_previous_by_date(published=True)
    except models.BlogPost.DoesNotExist:
        prev_post = None

    context = {
        'page': page,
        'next_page': next_post,
        'prev_page': prev_post,
    }

    return render(request, 'blog/post.html', context=context)


def post_res(request, post_url, res_url):
    """
    Serve resources belonging to the given post

    TODO: Do this in a less sketchy way -- probably copy / move images on load
    """
    assets: Path = settings.RESOURCEFILES_DIR / 'blog' / 'flatpages' / 'assets'
    image = assets / res_url

    if image.exists():
        return HttpResponse(image.open('rb').read(), content_type="image/png")
    else:
        raise Http404("The file you are looking for does not exist")

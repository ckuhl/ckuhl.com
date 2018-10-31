import logging

from django.http import Http404
from django.shortcuts import redirect, render

from blog.models import BlogPost


log = logging.getLogger(__name__)


def root(request):
    """Render the blog home page"""
    context = {'posts': BlogPost.objects.values().order_by('-date')[:3]}
    return render(request, 'blog/home.html', context=context)


def archive(request):
    """Render the archive of all pages"""
    # TODO: Limit and paginate blog posts (i.e. 25 or 50 per page?
    context = {'posts': BlogPost.objects.values().order_by('-date')}
    return render(request, 'blog/archive.html', context=context)


def old_archive(request):
    """Redirect to the new archive URL"""
    return redirect(archive, permanent=True)


def post(request, post_url):
    """Single blog post"""
    try:
        page = BlogPost.objects.get(url=post_url)
    except BlogPost.DoesNotExist:
        # TODO: Local analytics to log this to a DB table
        log.error(f"User tried to get page {post_url} that doesn't exist")
        raise Http404("The blog post you're looking for does not exist")

    return render(request, 'blog/post.html', context={'post': page})


def tags(request, tag_name):
    """List of all pages with a given tag"""
    # TODO: Create `tags` table and select from there
    # tagged = BlogPost.objects.values(tag=tag_name)[:25]
    return render(request, 'blog/tagged.html', context={'posts': []})


def rss(request):
    """Feed of latest blog posts"""
    # TODO: Render RSS feed using FeedGenerator
    # latest = BlogPost.objects.values().order_by('-date')[:25]
    raise Http404("The RSS feed hasn't been implemented yet. Sorry!")

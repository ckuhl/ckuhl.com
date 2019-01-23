from typing import List

from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.feedgenerator import Rss201rev2Feed, RssFeed

from blog import models


class BlogPostRssFeed(Feed):
    """RSS feed generator for the blog"""
    title: str = "Chris Kuhl's blog"
    description: str = 'The latest blog posts from ckuhl.com'
    link: str = reverse_lazy('blog:index')
    feed_type: RssFeed = Rss201rev2Feed

    def items(self) -> List[models.BlogPost]:
        return models.BlogPost.objects.order_by('-date')[:5]

    def item_title(self, item: models.BlogPost) -> str:
        return item.title

    def item_description(self, item: models.BlogPost) -> str:
        return item.body

    def item_link(self, item: models.BlogPost) -> str:
        return item.get_absolute_url()

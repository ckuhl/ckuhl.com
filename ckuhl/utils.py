import datetime
import json

from feedgen.feed import FeedGenerator
from peewee import TextField


BASE_URL = 'https://ckuhl.com/'


def create_feedgen(posts):
    """
    Create a FeedGenerator and fill in recent posts

    :param list(dict) posts: List of FlatPages pages
    :returns FeedGenerator: Initialized feedgenerator
    """
    fg = FeedGenerator()

    # init feed
    fg.title('Chris Kuhl\'s Blog')
    fg.author( {'name':'Chris Kuhl'})
    fg.description("A mix of technical posts and personal updates")
    fg.link( href='https://ckuhl.com/blog/rss/', rel='self' )
    fg.language('en')

    # add posts
    for post in posts[::-1]:
        fe = fg.add_entry()
        fe.id(BASE_URL + 'blog/' + post.path)
        fe.title(post.meta['title'])
        fe.published(post.meta['created'])
        fe.updated(post.meta['updated'])
        fe.content(post.html,type='html')
        fe.link(href=BASE_URL + 'blog/' + 'rss')

    return fg


def generate_rss_feed(posts):
    """
    Utility wrapper to create an RSS feed from a list of posts
    """
    fg = create_feedgen(posts)
    return fg.rss_str(pretty=True)


def get_pages(flatpages, n=999, is_published=True):
    """
    Get a list of n pages, optionally unpublished
    """
    # Articles are pages with a publication date
    articles = [p for p in flatpages if 'published' in p.meta and
                p.meta['published'] is is_published]
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['created'])
    return latest[:n]


class JSONField(TextField):
    """Store JSON data in a TextField."""
    def python_value(self, value):
        if value is not None:
            return json.loads(value)

    def db_value(self, value):
        if value is not None:
            return json.dumps(value)


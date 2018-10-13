import json
import logging
from pathlib import Path
from typing import List, Optional

from feedgen.feed import FeedGenerator
from flask import current_app, url_for
from flatterpages import FlatterPages, Page
from peewee import TextField


logger = logging.getLogger(__name__)


def root_dir() -> str:
    """Returns the root of the project"""
    return Path(__file__).parent.parent


def create_feed_generator(posts: List[Page]) -> FeedGenerator:
    """
    Create a FeedGenerator and fill in recent posts

    :param list(dict) posts: List of FlatPages pages
    :returns FeedGenerator: Initialized FeedGenerator
    """
    fg = FeedGenerator()

    # init feed
    fg.title("Chris Kuhl's Blog")
    fg.author({'name': 'Chris Kuhl'})
    fg.description("A mix of technical posts and personal updates")
    fg.link(href='https://ckuhl.com/blog/rss/', rel='self')
    fg.language('en')

    # add posts
    for post in posts[::-1]:
        fe = fg.add_entry()
        fe.id(url_for('blog.post', path=post.path))
        fe.title(post.meta['title'])
        fe.published(post.meta['created'])
        fe.updated(post.meta['updated'])
        fe.content(post.html, type='html')
        fe.link(href=current_app.config["BASE_URL"] + 'blog/' + 'rss')

    return fg


def generate_rss_feed(posts: List[Page]) -> str:
    """Create an RSS feed from a list of posts"""
    fg = create_feed_generator(posts)
    return fg.rss_str(pretty=True)


def get_pages(flatpages: FlatterPages,
              n: Optional[int] = None,
              include_unpublished: bool = False) -> List[Page]:
    """Get a list of Pages, sorted by age"""
    articles = [p for p in flatpages if 'published' in p.meta and
                p.meta['published'] is not include_unpublished]
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['created'])
    return latest[:n] if n else latest


def filter_by_category(flatpages: FlatterPages,
                       category: str,
                       n: Optional[int] = None,
                       include_unpublished: bool = False) -> List[Page]:
    """Get a list of Pages in a given category, sorted by age"""
    pages = get_pages(flatpages, include_unpublished=include_unpublished)
    category_pages = [p for p in pages if p.meta['category'] == category]
    return category_pages[:n] if n else category_pages


class JSONField(TextField):
    """Store JSON data in a TextField"""

    def python_value(self, value):
        """Deserialize from DB into a Python object"""
        if value is not None:
            return json.loads(value)

    def db_value(self, value):
        """Serialize from a Python object into a string"""
        if value is not None:
            return json.dumps(value)

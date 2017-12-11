import os
from os.path import dirname, abspath


BASE_DIR = dirname(dirname(abspath(__file__)))

class BaseConfig:
    FLATPAGES_BLOG_ROOT = os.path.join('..', 'content', 'blog')
    FLATPAGES_BLOG_AUTO_RELOAD = False
    FLATPAGES_BLOG_EXTENSION = '.md'
    FLATPAGES_BLOG_MARKDOWN_EXTENSIONS = [
            'abbr',
            'codehilite',
            'smarty',
            'footnotes',
    ]

    FLATPAGES_PORTFOLIO_ROOT = os.path.join('..', 'content', 'projects')
    FLATPAGES_PORTFOLIO_AUTO_RELOAD = False
    FLATPAGES_PORTFOLIO_EXTENSION = '.md'
    FLATPAGES_PORTFOLIO_MARKDOWN_EXTENSIONS = [
            'abbr',
            'codehilite',
            'smarty',
            'footnotes',
    ]


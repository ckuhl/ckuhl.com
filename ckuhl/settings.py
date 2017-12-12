import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseConfig:
    FLATPAGES_BLOG_ROOT = os.path.join('..', 'flatpages', 'blog')
    FLATPAGES_BLOG_EXTENSION = '.md'
    FLATPAGES_BLOG_MARKDOWN_EXTENSIONS = [
            'abbr',
            'codehilite',
            'smarty',
            'footnotes',
    ]

    FLATPAGES_PORTFOLIO_ROOT = os.path.join('..', 'flatpages', 'portfolio')
    FLATPAGES_PORTFOLIO_EXTENSION = '.md'
    FLATPAGES_PORTFOLIO_MARKDOWN_EXTENSIONS = [
            'abbr',
            'codehilite',
            'smarty',
            'footnotes',
    ]


class ProdConfig(BaseConfig):
    DEBUG = False
    FLATPAGES_BLOG_AUTO_RELOAD = False
    FLATPAGES_PORTFOLIO_AUTO_RELOAD = False


class DebugConfig(BaseConfig):
    DEBUG = True
    FLATPAGES_BLOG_AUTO_RELOAD = True
    FLATPAGES_PORTFOLIO_AUTO_RELOAD = True


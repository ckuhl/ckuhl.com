import os


class BaseConfig:
    # project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATABASE_NAME = os.path.join(BASE_DIR, 'analytics.sqlite')

    # logging
    LOG_NAME = 'application.log'

    # FlatPages 'blog' settings
    ## flatpages only uses relative paths
    FLATPAGES_BLOG_ROOT = os.path.join('..', 'flatpages', 'blog')
    FLATPAGES_BLOG_EXTENSION = '.md'
    FLATPAGES_BLOG_MARKDOWN_EXTENSIONS = [
            'abbr',
            'codehilite',
            'smarty',
            'footnotes',
    ]

    # FlatPages 'portfolio' settings
    ## flatpages only uses relative paths
    FLATPAGES_PORTFOLIO_ROOT = os.path.join('..', 'flatpages', 'portfolio')
    FLATPAGES_PORTFOLIO_EXTENSION = '.md'
    FLATPAGES_PORTFOLIO_MARKDOWN_EXTENSIONS = [
            'abbr',
            'codehilite',
            'smarty',
            'footnotes',
    ]


class ProdConfig(BaseConfig):
    # debugging
    DEBUG = False

    # FlatPages debugging
    FLATPAGES_BLOG_AUTO_RELOAD = False
    FLATPAGES_PORTFOLIO_AUTO_RELOAD = False


class DebugConfig(BaseConfig):
    # debugging
    DEBUG = True

    # FlatPages debugging
    FLATPAGES_BLOG_AUTO_RELOAD = True
    FLATPAGES_PORTFOLIO_AUTO_RELOAD = True


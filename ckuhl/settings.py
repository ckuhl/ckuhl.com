import os


class BaseConfig:
    # project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Database location
    DATABASE_NAME = os.path.join(BASE_DIR, 'analytics.sqlite')

    # logging
    LOG_NAME = 'application.log'

    # FlatPages settings
    # note: Flask-FlatPages only uses relative paths
    FLATPAGES_BLOG_ROOT = os.path.join('..', 'flatpages')
    FLATPAGES_BLOG_EXTENSION = '.md'
    FLATPAGES_BLOG_MARKDOWN_EXTENSIONS = [
        # allows script tags in markdown
        'extra',
        # define abbreviations (e.g. HTML, W3C, &c.)
        'abbr',
        # code highlighting
        'codehilite(linenums=True)',
        # use ``` to denote code (instead of spaces)
        'fenced_code',
        # convert ASCII dashes/quotes/ellipses to HTML equiv.
        'smarty',
        # use [^<label>] to use footnotes inline
        'footnotes',
    ]


class ProdConfig(BaseConfig):
    """Configuration for running on production"""
    DEBUG = False
    FLATPAGES_AUTO_RELOAD = False
    BASE_URL = 'https://ckuhl.com/'


class DebugConfig(BaseConfig):
    """Configuration for running locally (i.e. debugging)"""
    DEBUG = True
    FLATPAGES_AUTO_RELOAD = True
    BASE_URL = 'http://127.0.0.1:5000/'

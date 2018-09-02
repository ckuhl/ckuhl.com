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
            'extra',  # allows script tags in markdown
            'abbr',  # define abbreviations (e.g. HTML, W3C, &c.)
            'codehilite(linenums=True)',  # code highlighting
            'fenced_code',  # use ``` to denote code (instead of spaces)
            'smarty',  # convert ASCII dashes/quotes/ellipses to HTML equiv.
            'footnotes',  # use [^<label>] to define footnotes inline
    ]


class ProdConfig(BaseConfig):
    # debugging
    DEBUG = False

    # FlatPages debugging
    FLATPAGES_AUTO_RELOAD = False


class DebugConfig(BaseConfig):
    # debugging
    DEBUG = True

    # FlatPages debugging
    FLATPAGES_AUTO_RELOAD = True


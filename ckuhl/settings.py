import os


class BaseConfig:
    # project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATABASE_NAME = os.path.join(BASE_DIR, 'analytics.sqlite')

    # logging
    LOG_NAME = 'application.log'

    # FlatPages settings
    ## flatpages only uses relative paths
    FLATPAGES_ROOT = os.path.join('..', 'flatpages')
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_MARKDOWN_EXTENSIONS = [
            'abbr',
            'codehilite',
            'smarty',
            'footnotes',
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


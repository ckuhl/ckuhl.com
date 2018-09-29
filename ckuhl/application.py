import logging
import os
from importlib import import_module

from flask import Flask

from .ext import Database, Pages
from .models import PageView
from .settings import DebugConfig, ProdConfig
from .views import analytics, blog, core, portfolio, shortlinks


def create_app(debug=False):
    """
    Constructor for the Flask application

    :param bool debug: Flag to enable debugging mode
    :returns Flask: Flask application object
    """
    # set configuration
    if debug:
        config = DebugConfig
    else:
        config = ProdConfig

    # initialize app
    app = Flask(__name__,
                template_folder=os.path.join(config.BASE_DIR, 'templates'),
                static_folder=os.path.join(config.BASE_DIR, 'static'))

    # configure app
    app.config.from_object(config)

    # set logging
    logging.basicConfig(filename=config.LOG_NAME, level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # import middleware
    with app.app_context():
        import_module('ckuhl.middleware')  # TODO: Replace with relative import?

    # register blueprints
    app.register_blueprint(blog.blog, url_prefix='/blog')
    app.register_blueprint(portfolio.portfolio, url_prefix='/portfolio')
    app.register_blueprint(shortlinks.short_links, url_prefix='/s')
    app.register_blueprint(core.core)
    app.register_blueprint(analytics.analytics)

    # initialize extensions
    Database.create_tables([PageView], safe=True)
    Pages.init_app(app)

    return app

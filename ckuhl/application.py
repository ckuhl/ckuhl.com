import logging
from importlib import import_module

import yaml
from flask import Flask

from .ext import Database, Pages
from .models import PageView
from .settings import DebugConfig, ProdConfig
from .views import analytics, blog, core, portfolio, shortlinks


logger = logging.getLogger(__name__)


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
                template_folder='templates',
                static_folder=config.BASE_DIR / 'static')

    # load default configuration
    app.config.from_object(config)

    # load secrets configuration
    secrets = app.config["BASE_DIR"] / "secrets" / "default.secret.yml"
    if not secrets.is_file():
        secrets = app.config["BASE_DIR"] / "secrets" / "default.yml"
    app.config.from_mapping(yaml.load(open(secrets)))

    # set logging
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(filename=config.LOGFILE_NAME, level=logging.INFO)

    # import middleware
    with app.app_context():
        import_module('..middleware', package=__name__)

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

import logging
import os

from flask import Flask, abort, render_template, request
from flask_flatpages import FlatPages

from . import jinja_filters
from . import tools
from .blog import blog
from .root import root
from .portfolio import portfolio
from .extensions import Blog, Portfolio
from .settings import BASE_DIR, ProdConfig, DebugConfig


def create_app(debug=False):
    """
    Constructor for the Flask application

    :param bool debug: Flag to enable debugging mode
    :returns Flask: Flask application object
    """
    # init logging
    logging.basicConfig(filename='flask.log',level=logging.DEBUG)
    logger = logging.getLogger(__name__)  # for requests

    # init app
    app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

    # configure settings
    if debug:
        Config = DebugConfig
    else:
        Config = ProdConfig
    app.config.from_object(Config)

    # import jinja filters
    # TODO: Simplify this (move to middleware?)
    app.jinja_env.filters['datetimeformat'] = jinja_filters.datetimeformat

    # import blueprints
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(portfolio, url_prefix='/portfolio')
    app.register_blueprint(root)

    # HTTP error codes
    # TODO: Move this to middleware?
    @app.errorhandler(404)
    def page_404(e):
        """Page not found"""
        return render_template('errors/404.html'), 404

    @app.errorhandler(403)
    def page_403(e):
        """Forbidden"""
        return render_template('errors/403.html'), 403

    # request hooks (more for middleware!)
    @app.before_request
    def log_request():
        """
        Log all visiting user agents
        """
        logger.info("%s %s", request.user_agent, request.accept_languages)


    # init extensions
    Blog.init_app(app)
    Portfolio.init_app(app)

    return app


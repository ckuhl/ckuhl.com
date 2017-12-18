import datetime
import logging
import os

from flask import Flask, abort, render_template, request
from flask_flatpages import FlatPages

from . import jinja_filters

from .ext import Database, Blog, Portfolio
from .settings import ProdConfig, DebugConfig
from .models import PageView

from .views import analytics, blog, root, portfolio, tools, travel


def create_app(debug=False):
    """
    Constructor for the Flask application

    :param bool debug: Flag to enable debugging mode
    :returns Flask: Flask application object
    """
    # configuration
    if debug:
        config = DebugConfig
    else:
        config = ProdConfig

    # init app
    app = Flask(__name__,
            template_folder=os.path.join(config.BASE_DIR, 'templates'),
            static_folder=os.path.join(config.BASE_DIR, 'static'))

    # configure app
    app.config.from_object(config)

    # init logging
    logging.basicConfig(filename=config.LOG_NAME, level=logging.DEBUG)
    logger = logging.getLogger(__name__)  # for requests

    # import jinja filters
    # TODO: Simplify this (move to middleware?)
    app.jinja_env.filters['datetimeformat'] = jinja_filters.datetimeformat
    app.jinja_env.filters['teaser_para'] = jinja_filters.teaser_para
    app.jinja_env.filters['teaser_sentence'] = jinja_filters.teaser_sentence

    # import blueprints
    app.register_blueprint(blog.blog, url_prefix='/blog')
    app.register_blueprint(travel.travel, url_prefix='/travel')
    app.register_blueprint(portfolio.portfolio, url_prefix='/portfolio')
    app.register_blueprint(tools.utilities, url_prefix='/tools')
    app.register_blueprint(root.root)
    app.register_blueprint(analytics.analytics)

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
        logger.info("%s # %s # %s # %s",
                request.user_agent,
                request.accept_languages,
                request.url,
                datetime.datetime.now())


    # init extensions
    Database.create_tables([PageView], safe=True)
    Blog.init_app(app)
    Portfolio.init_app(app)

    return app


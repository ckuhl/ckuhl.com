import logging
import os

from flask import Flask
from flask import abort
from flask import render_template
from flask_flatpages import FlatPages

from . import jinja_filters
from . import tools
from .blog import blog
from .root import root
from .portfolio import portfolio
from .extensions import Blog, Portfolio
from .settings import BASE_DIR, BaseConfig


def create_app():
    """
    Create the Flask application
    """
    logger = logging.getLogger(__name__)

    # Flatpages config
    app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

    app.config.from_object(BaseConfig)

    app.jinja_env.filters['prettydate'] = jinja_filters.prettydate
    app.jinja_env.filters['numericdate'] = jinja_filters.numericdate


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

    # initialize extensions
    Blog.init_app(app)
    Portfolio.init_app(app)

    print(Blog.root)

    return app


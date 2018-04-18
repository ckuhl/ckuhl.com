from flask import Blueprint, render_template
from flask_flatpages import FlatPages

from .. import utils
from ..ext import Wiki


wiki = Blueprint('wiki', __name__)

@wiki.route('/', defaults={'path': ''})
@wiki.route('/<path:path>')
def home(path):
    # get page
    p = Wiki.get(path)
    if p is None:
        p = Wiki.get_or_404(path + 'index')
    return render_template('wiki/page.j2', content=p)


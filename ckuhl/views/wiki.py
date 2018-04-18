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

    # create URL heirarchy
    tree = path.split('/')
    new_tree = []
    for i in len(tree) - 1:
        new_tree.append(tree[:i + 1].join('/'))

    return render_template('wiki/page.j2', content=p, parents=new_tree)


import base64

from flask import Blueprint, Response, abort, current_app, request

from ..ext import Database
from ..models import PageView


BEACON = base64.b64decode(
    'R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==')

JAVASCRIPT = """(function(){
var d=document,i=new Image,e=encodeURIComponent;
i.src='%s/background.gif?url='+e(d.location.href)+'&ref='+e(d.referrer)+'&t='+e(d.title);
})()""".replace('\n', '')

analytics = Blueprint('analytics', __name__)


@analytics.route('/background.gif')
def analyze():
    if not request.args.get('url'):
        abort(404)

    with Database.transaction():
        PageView.create_from_request()

    response = Response(BEACON, mimetype='image/gif')
    response.headers['Cache-Control'] = 'private, no-cache'
    return response


@analytics.route('/custom.js')
def script():
    return Response(
        JAVASCRIPT % current_app.config["BASE_URL"],
        mimetype='text/javascript')

import base64

from flask import abort, Blueprint, Response, request

from .models import PageView
from .extensions import Database


BEACON = base64.b64decode('R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==')

JAVASCRIPT = """(function(){
var d=document,i=new Image,e=encodeURIComponent;
i.src='%s/a.gif?url='+e(d.location.href)+'&ref='+e(d.referrer)+'&t='+e(d.title);
})()""".replace('\n', '')

analytics = Blueprint('analytics', __name__)

@analytics.route('/a.gif')
def analyze():
    if not request.args.get('url'):
        abort(404)

    with Database.transaction():
        PageView.create_from_request()

    response = Response(BEACON, mimetype='image/gif')
    response.headers['Cache-Control'] = 'private, no-cache'
    return response

@analytics.route('/a.js')
def script():
    return Response(
            JAVASCRIPT % 'https://ckuhl.com',  # TODO: Replace with proper var
            mimetype='text/javascript')


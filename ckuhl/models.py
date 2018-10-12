import datetime
from urllib.parse import parse_qsl, urlparse

from flask import request
from peewee import CharField, DateTimeField, Model, TextField

from .ext import Database
from .utils import JSONField


class BaseModel(Model):
    """Now all models are connected to the database by default"""

    class Meta:
        database = Database


class PageView(BaseModel):
    """Representation of a page view on my website"""
    domain = CharField()
    url = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)
    title = TextField(default='')
    ip = CharField(default='')
    referrer = TextField(default='')
    headers = JSONField()
    params = JSONField()

    @classmethod
    def create_from_request(cls):
        """Create a PageView object / entry directly from the query string"""
        parsed = urlparse(request.args['url'])
        params = dict(parse_qsl(parsed.query))

        return PageView.create(
            domain=parsed.netloc,
            url=parsed.path,
            title=request.args.get('t') or '',
            ip=request.headers.get('X-Forwarded-For', request.remote_addr),
            referrer=request.args.get('ref') or '',
            headers=dict(request.headers),
            params=params)

import datetime
import urllib

from flask import request
from peewee import Model, CharField, TextField, DateTimeField

from .extensions import Database
from .tools import JSONField


class BaseModel(Model):
    class Meta:
        database = Database


class PageView(BaseModel):
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
        parsed = urllib.parse.urlparse(request.args['url'])
        params = dict(urllib.parse.parse_qsl(parsed.query))

        return PageView.create(
            domain=parsed.netloc,
            url=parsed.path,
            title=request.args.get('t') or '',
            ip=request.headers.get('X-Forwarded-For', request.remote_addr),
            referrer=request.args.get('ref') or '',
            headers=dict(request.headers),
            params=params)


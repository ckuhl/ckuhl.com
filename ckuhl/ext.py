from flask_flatpages import FlatPages
from peewee import SqliteDatabase

from .settings import BaseConfig


Database = SqliteDatabase(BaseConfig.DATABASE_PATH)
Pages = FlatPages(name='blog')

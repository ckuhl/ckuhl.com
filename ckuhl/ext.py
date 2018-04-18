from flask_flatpages import FlatPages
from peewee import SqliteDatabase

from .settings import BaseConfig


Database = SqliteDatabase(BaseConfig.DATABASE_NAME)
Pages = FlatPages(name='blog')
Wiki = FlatPages(name='wiki')


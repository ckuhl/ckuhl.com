from flatterpages import FlatterPages
from peewee import SqliteDatabase

from .settings import BaseConfig


Database = SqliteDatabase(str(BaseConfig.DATABASE_PATH))
Pages = FlatterPages(name='blog')

from peewee import *
from settings import settings


settings = settings()


class BaseModel(Model):
    class Meta:
        database = settings.db

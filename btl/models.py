from django.db import models
import mongoengine as db


# Create your models here.

class Users(db.Document):
    username = db.StringField()
    password = db.StringField()
    name = db.StringField()

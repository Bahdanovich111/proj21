from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField


class SomeData(models.Model):
    print('model')
    data = JSONField()

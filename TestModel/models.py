# models.py
from django.db import models
class Test(models.Model):
    name = models.CharField(max_length=256)
    def __unicode__(self):
        return self.name



# Create your models here.

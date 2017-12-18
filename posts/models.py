from __future__ import unicode_literals
from django.db import models

# Create your models here.
#MVC
#MODEL VIEW CONTROL

class Post(models.Model):
    title =models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = True,auto_now_add = False)
    updated = models.DateTimeField(auto_now=False,auto_now_add=True)
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


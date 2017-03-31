from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mailer(models.Model):
    to_address = models.TextField(blank=True,null=True)
    from_address = models.CharField(max_length=200,blank=True,null=True)
    subject = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=200,blank=True,null=True)
    priority = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.subject)

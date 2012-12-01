from django.db import models

# Create your models here.

class Fortune(models.Model):
    text = models.TextField('Fortune')

    def __unicode__(self):
        return '%s ...' % (self.text[:40])

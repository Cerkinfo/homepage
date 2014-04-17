# -*- coding: utf-8 -*- #
from django.db import models

YEAR = '201314'

REUNION_TYPES = (
        ('', 'Réunion normale'),
        ('B', 'Réunion du bureau'),
        ('AG', 'Assemblée générale élective'),
        )

NICE_TYPE = { '': u'Réunion',
                'B': u'Réunion du bureau ',
                'AG' : u'Assemblée générale élective '
               }

def determine_name(obj, filename):
    type_text = '-' + obj.reunion_type if obj.reunion_type else ''
    return "pv/%s/%s%s.pdf" % (obj.year, obj.date.isoformat(), type_text)

class PV(models.Model):
    pvfile = models.FileField(upload_to=determine_name)
    date = models.DateField('Date de la reunion')
    reunion_type = models.CharField('Type de réunion', max_length=2, choices=REUNION_TYPES, default='', blank=True)
    year = models.CharField("Année de comité du pv", max_length=6, default=YEAR)

    def __unicode__(self):
       return '%s du %s' % (
                    NICE_TYPE[self.reunion_type],
                    self.date.strftime('%d/%m/%Y'))


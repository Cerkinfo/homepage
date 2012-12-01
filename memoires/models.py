# -*- coding: utf-8 -*- #
from django.db import models


def determine_name(obj, filename):
    return "memoires/%s/%s" % (obj.year, filename)

class Memoire(models.Model):
    fileobj = models.FileField('Fichier mémoire', upload_to=determine_name)
    author = models.CharField('Auteur', max_length=100)
    subject = models.CharField('Sujet', max_length=700)
    year = models.IntegerField("Année")

    def __unicode__(self):
       return 'Memoire %s de %s' % (self.subject, self.author)

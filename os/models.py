# -*- coding: utf-8 -*- #
from django.db import models
from django.conf import settings
import os
from os.path import dirname, exists
import commands
import logging

def determine_name(obj, filename):
    return "os/%s/%s_%s_%s.pdf" % (obj.comiteyear, obj.comiteyear, obj.numero, obj.title)

class OS(models.Model):
    fileobj = models.FileField('Fichier OS', upload_to=determine_name)
    title = models.CharField('Titre (ie StV, Elections)', max_length=60)
    comiteyear = models.IntegerField("Année de comité", default=201011)
    numero = models.IntegerField("Numéro de l'OS")
    private = models.BooleanField("OS caché (ex:OS censuré)", default=False)

    def __unicode__(self):
       return u'OS %s %s %s' % (self.comiteyear,  self.numero, self.title)

    def name(self):
       return u'%s %s %s' % (self.numero, self.comiteyear, self.comiteyear)

    def thumbnail_path(self):
       return "%s/thumbs/%s.png" % (settings.MEDIA_ROOT, self.fileobj.name)

    def thumbnail_url(self):
       return "%s/thumbs/%s.png" % (settings.MEDIA_URL, self.fileobj.name)

    def generate_thumbnail(self):
        thumb_dir = dirname(self.thumbnail_path())
        if not exists(thumb_dir):
            os.makedirs(thumb_dir)
        
        cmd = "convert -resize 100 %s[0] %s" % (self.fileobj.path, self.thumbnail_path())
        print cmd
        status, output = commands.getstatusoutput(cmd)

        if status != 0:
            logging.error("%s<-IMAGEMAGICK RETURNED STATUS %s" % (original_image_path, status))

    def save(self, *args, **kwargs):
        super(OS, self).save(*args, **kwargs) # Call the "real" save() method.
        self.generate_thumbnail()



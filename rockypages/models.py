from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    content = RichTextField()
    url = models.CharField('URL', max_length=100, db_index=True)
    title = models.CharField('title', max_length=200)


# -*- coding: utf-8 -*- #
from ci.memoire.models import Memoire
from django.contrib.syndication.views import Feed

class LatestMemoiresFeed(Feed):
    title = "Dernier Memoires rajoutés"
    link = "/memoires/"
    description = "Dernier mémoires rajouté sur le site du Cercle Informatique"

    def items(self):
        return Memoires.objects.all().order_by('-date')[:10]

    def item_link(self, item):
        return item.fileobj.url


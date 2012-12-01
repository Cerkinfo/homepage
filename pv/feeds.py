# -*- coding: utf-8 -*- #
from ci.pv.models import PV
from django.contrib.syndication.views import Feed

class LatestPVFeed(Feed):
    title = "Dernier PVs"
    link = "/pv/"
    description = "Dernier procès-verbaux du Cercle Informatique"

    def items(self):
        return PV.objects.all().order_by('-date')[:10]

    def item_link(self, item):
        return item.pvfile.url


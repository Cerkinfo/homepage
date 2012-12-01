from django.conf.urls.defaults import *
from ci.pv.feeds import LatestPVFeed
from ci.pv.models import PV

pv_dict = {
    'queryset': PV.objects.all().order_by('-date')
    }

#urlpatterns = patterns('ci.pv.views',
#    (r'^$', 'this_year'),
#    )

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', pv_dict),
    (r'^rss/$', LatestPVFeed()),
    )

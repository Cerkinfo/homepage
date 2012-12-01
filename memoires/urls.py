from django.conf.urls.defaults import *
from ci.memoires.models import Memoire

all_dict = {
            'queryset': Memoire.objects.all().order_by('-year'),
            }

urlpatterns = patterns(None,
    (r'^$', 'django.views.generic.list_detail.object_list', all_dict),
    )

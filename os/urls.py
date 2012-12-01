from django.conf.urls.defaults import *
from ci.os.models import OS

all_dict = {
            'queryset': OS.objects.all().order_by('-comiteyear', '-numero'),
            }

urlpatterns = patterns(None,
    (r'^$', 'django.views.generic.list_detail.object_list', all_dict),
    )

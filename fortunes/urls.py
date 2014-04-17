from django.conf.urls.defaults import *
from ci.fortunes.models import Fortune

fortune_dict = {
            'queryset': Fortune.objects.all()
            }

txt_dict = {
            'queryset': Fortune.objects.all(),
            'template_name': 'fortunes/fortune_txt.html',
	    'mimetype': 'text/plain',
            }

all_dict = {
            'queryset': Fortune.objects.all().order_by('-id'),
            'paginate_by': 30
            }


urlpatterns = patterns(None,
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', fortune_dict),
    (r'^(?P<object_id>\d+)/CI.txt/$', 'django.views.generic.list_detail.object_list', txt_dict),
    (r'^CI.txt/$', 'django.views.generic.list_detail.object_list', txt_dict),
    (r'^$', 'django.views.generic.list_detail.object_list', all_dict),
    )


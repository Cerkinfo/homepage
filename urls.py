from django.conf.urls.defaults import *
from django.conf import settings



from django.contrib import admin
admin.autodiscover()

from ci.feeds import LatestNewsFeed
from phpbb.models import PhpbbTopic

NEWS_FORUM_ID = getattr(settings, 'PHPBB_NEWS_FORUM_ID', -1)

test_dict = {
        'queryset': PhpbbTopic.objects.filter(forum__pk=NEWS_FORUM_ID).all()[:5],
    'template_name' : 'test-news.html'
    }

news_dict = {
        'queryset': PhpbbTopic.objects.filter(forum__pk=NEWS_FORUM_ID).order_by('-topic_time_int').all()[:5],
    'template_name' : 'news.html'
    }


urlpatterns = patterns('',
    # Example:
    # (r'^ci/', include('ci.foo.urls')),
#    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': '/home/olivier/ci.media'}),


    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^pv/', include('ci.pv.urls')),
    (r'^memoires/', include('ci.memoires.urls')),
    (r'^os/', include('ci.os.urls')),
    (r'^fortunes/', include('ci.fortunes.urls')),
    (r'^404/$', 'ci.views.error_404_random_fortune'),
    (r'^rss/$', LatestNewsFeed()),
    (r'^rss_news.php/$', LatestNewsFeed()),
#    (r'^news/rss/(?P<forum_id>\d+)$', LatestNewsFeed()),
    (r'^frontendadmin/', include('frontendadmin.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^test/$', 'django.views.generic.list_detail.object_list', test_dict),
    (r'^$', 'django.views.generic.list_detail.object_list', news_dict),
)

handler404 = 'ci.views.error_404_random_fortune'

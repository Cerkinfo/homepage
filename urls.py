from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

from feeds import LatestNewsFeed
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
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^ckeditor/', include('ckeditor.urls')),

    (r'^pv/', include('pv.urls')),
    (r'^memoires/', include('memoires.urls')),
    (r'^os/', include('os.urls')),
    (r'^fortunes/', include('fortunes.urls')),
    (r'^404/$', 'views.error_404_random_fortune'),
    (r'^rss/$', LatestNewsFeed()),
    (r'^rss_news.php/$', LatestNewsFeed()),
    (r'^frontendadmin/', include('frontendadmin.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^$', 'django.views.generic.list_detail.object_list', news_dict),
)
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DIR}),
	)

handler404 = 'views.error_404_random_fortune'

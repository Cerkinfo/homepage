# -*- coding: utf-8 -*- #
from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.shortcuts import get_object_or_404
from django.conf import settings

from phpbb.models import PhpbbForum, PhpbbTopic
from phpbb.templatetags.phpbb import bbcode


NEWS_FORUM_ID = getattr(settings, 'PHPBB_NEWS_FORUM_ID', -1)

class LatestNewsFeed(Feed):
    title = "Cercle Informatiques"
    link = "/news/"
    description = "Dernieres nouvelles du Cercle Informatique"

    def get_object(self, request, forum_id=NEWS_FORUM_ID):
        return get_object_or_404(PhpbbForum, pk=forum_id)

    def items(self, obj):
        return PhpbbTopic.objects.filter(forum=obj).order_by('-topic_time_int')

    def item_link(self, obj):
        return obj.get_external_url()

    def item_description(self, obj):
        return bbcode(obj.topic_first_post.post_text)


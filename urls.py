from django.conf.urls import patterns, url
from django.conf import settings

import dashboard.views

urlpatterns = patterns('',
    url(r'^$', dashboard.views.DashboardView.as_view(), name='dashboard-index'),
    url(r'^result$', dashboard.views.TopicsView.as_view(), name='result'),
    url(r'^posts/(?P<group_id>\d+)$', dashboard.views.PostsView.as_view(), name='group-info'),
    url(r'^posts/post_content$', dashboard.views.CreatePostView.as_view(), name='group-info'),
    url(r'^posts/result$', dashboard.views.CreatePostContentView.as_view(), name='group-info'),
    url(r'^create_topic$', dashboard.views.CreateTopicView.as_view(), name='group-info'),

)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

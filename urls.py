from django.conf.urls import patterns, url
from django.conf import settings

import dashboard.views

urlpatterns = patterns('',
    url(r'^$', dashboard.views.DashboardView.as_view(), name='dashboard-index'),
    url(r'^result$', dashboard.views.ResultView.as_view(), name='result'),
    url(r'^group/(?P<group_id>\d+)$', dashboard.views.GroupInfoView.as_view(), name='group-info'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

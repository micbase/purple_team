from django.conf.urls import patterns, url

import dashboard.views

urlpatterns = patterns('',
    url(r'^$', dashboard.views.DashboardView.as_view(), name='dashboard-index'),
)

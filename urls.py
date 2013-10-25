from django.conf.urls import patterns, url
from django.conf import settings

import dashboard.views
import auth.views

urlpatterns = patterns('',
    url(r'^$', dashboard.views.ResultView.as_view(), name='course-list'),
    url(r'^topics/(?P<class_id>\d+)$', dashboard.views.TopicsView.as_view(), name='topics'),
    url(r'^create_topic/(?P<class_id>\d+)$', dashboard.views.CreateTopicView.as_view(), name='create_topic'),
    url(r'^posts/(?P<topic_id>\d+)$', dashboard.views.PostsView.as_view(), name='group-info'),
    url(r'^posts/post_content$', dashboard.views.CreatePostView.as_view(), name='group-info'),

    url(r'^login$', auth.views.LoginView.as_view(), name='login'),
    url(r'^logout$', auth.views.LogoutView.as_view(), name='logout'),
    url(r'^register$', auth.views.RegisterView.as_view(), name='register'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

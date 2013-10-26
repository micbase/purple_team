from django.conf.urls import patterns, url
from django.conf import settings

import dashboard.views
import auth.views

urlpatterns = patterns('',
    url(r'^$', dashboard.views.CourseView.as_view(), name='course_list'),

    url(r'^topics/(?P<course_id>\d+)$', dashboard.views.TopicsView.as_view(), name='topics'),
    url(r'^create_topic/(?P<course_id>\d+)$', dashboard.views.CreateTopicView.as_view(), name='create_topic'),

    url(r'^posts/(?P<topic_id>\d+)$', dashboard.views.PostsView.as_view(), name='group-info'),
    url(r'^posts/post_content$', dashboard.views.CreatePostView.as_view(), name='group-info'),

    url(r'^login$', auth.views.LoginView.as_view(), name='login'),
    url(r'^logout$', auth.views.LogoutView.as_view(), name='logout'),
    url(r'^register$', auth.views.RegisterView.as_view(), name='register'),

    url(r'^send_notification$', dashboard.views.NotificationView.as_view(), name='send_notification'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import SlackAuthView


urlpatterns = [
    url('login/', SlackAuthView.as_view(), name='slack_auth'),
]

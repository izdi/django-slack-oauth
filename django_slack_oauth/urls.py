# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import SlackAuthView, DefaultSuccessView


urlpatterns = [
    url('login/', SlackAuthView.as_view(), name='slack_auth'),
    url('success/', DefaultSuccessView.as_view(), name='slack_success')
]

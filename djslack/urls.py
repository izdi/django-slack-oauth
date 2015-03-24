from django.conf.urls import patterns, url

from .views import SlackAuthView, ForStartersView

urlpatterns = patterns('',
                       url('auth$', SlackAuthView.as_view(), name='slack_auth'),
                       )

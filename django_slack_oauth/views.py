# -*- coding: utf-8 -*-

import uuid
import urllib

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

import requests

from . import settings
from .models import SlackUser


class StateMismatch(Exception):
    pass


class SlackAuthView(RedirectView):
    permanent = True

    text_error = 'Attempt to update has failed. Please try again.'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SlackAuthView, self).dispatch(request, *args, **kwargs)

    @property
    def cache_key(self):
        return 'slack:' + str(self.request.user)

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if not code:
            return self.auth_request()

        self.validate_state(request.GET.get('state'))

        access_content = self.oauth_access(code)
        if not access_content.status_code == 200:
            return self.error_message()

        api_data = access_content.json()
        if not api_data['ok']:
            return self.error_message(api_data['error'])

        slacker, _ = SlackUser.objects.get_or_create(slacker=request.user)
        slacker.access_token = api_data.pop('access_token')
        slacker.extras = api_data
        slacker.save()

        messages.add_message(request, messages.SUCCESS, 'Your account has been successfully updated with '
                                                        'Slack. You can share your messages within your slack '
                                                        'domain.')

        return self.response()

    def auth_request(self):
        state = self.store_state()

        params = urllib.urlencode({
            'client_id': settings.SLACK_CLIENT_ID,
            'redirect_uri': self.request.build_absolute_uri(reverse('slack_auth')),
            'scope': settings.SLACK_SCOPE,
            'state': state,
        })

        return self.response(settings.SLACK_AUTHORIZATION_URL + '?' + params)

    def oauth_access(self, code):
        params = {
            'client_id': settings.SLACK_CLIENT_ID,
            'client_secret': settings.SLACK_CLIENT_SECRET,
            'code': code,
            'redirect_uri': self.request.build_absolute_uri(reverse('slack_auth')),
        }

        return requests.get(settings.SLACK_OAUTH_ACCESS_URL, params=params)

    def validate_state(self, state):
        state_before = cache.get(self.cache_key)
        cache.delete(self.cache_key)
        if state_before != state:
            raise StateMismatch('State mismatch upon authorization completion.'
                                ' Try new request.')
        return True

    def store_state(self):
        state = str(uuid.uuid4())[:6]
        cache.set(self.cache_key, state)
        return state

    def error_message(self, msg=text_error):
        messages.add_message(self.request, messages.ERROR, '%s' % msg)
        return self.response()

    def response(self, redirect=settings.SLACK_SUCCESS_REDIRECT_URL):
        return HttpResponseRedirect(redirect)

import json
import urllib

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, TemplateView
from django.contrib import messages

import requests

from .models import SlackUser


class ForStartersView(TemplateView):
    template_name = 'landing.html'


class SlackAuthView(RedirectView):
    text_error = 'Attempt to update has failed. Please try again.'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SlackAuthView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if not code:
            return self.auth_request()
        access_content = self.oauth_access(code)
        if not access_content.status_code == 200:
            return self.error_message()
        api_data = access_content.json()
        if not api_data['ok']:
            return self.error_message(api_data['error'])
        slacker = SlackUser.objects.get_or_create(slacker=request.user)[0]
        slacker.access_token = api_data['access_token']
        slacker.save()
        messages.add_message(self.request, messages.SUCCESS, 'Your account has been successfully updated with '
                                                             'Slack. You can share your messages within your slack '
                                                             'domain.')
        return self.response()

    def auth_request(self):
        params = urllib.urlencode({
            'client_id': settings.SLACK_CLIENT_ID,
            'redirect_uri': self.request.build_absolute_uri(reverse('slack_auth')),
            'scope': 'identify,read,post,client',
        })
        return self.response(settings.SLACK_AUTHORIZATION_URL + '?' + params)

    def oauth_access(self, code):
        params = {
            'client_id': settings.SLACK_CLIENT_ID,
            'client_secret': settings.SLACK_CLIENT_SECRET,
            'code': code,
            'redirect_uri': self.request.build_absolute_uri(reverse('slack_auth'))
        }
        return requests.get(settings.SLACK_OAUTH_ACCESS, params=params)

    def error_message(self, msg=text_error):
        messages.add_message(self.request, messages.ERROR, '%s' % msg)
        return self.response()

    def response(self, redirect='/'):
        return HttpResponseRedirect(redirect)
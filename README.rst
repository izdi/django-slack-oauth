======================================
Django Slack Oauth
======================================

Django module for handling Slack OAuth

Installation
============

* Add 'djslack' to your INSTALLED_APPS settings:

`
INSTALLED_APPS = (
    ...
    'djslack',
)
`

* Run `./manage syncdb` to add table for storing token

* Include the djslack URLconf in your project urls.py:

`url(r'^slack/', include('djslack.urls')),`

*. Set up settings

`
SLACK_CLIENT_ID = os.environ.get('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.environ.get('SLACK_CLIENT_SECRET')
SLACK_AUTHORIZATION_URL = 'https://slack.com/oauth/authorize'
SLACK_OAUTH_ACCESS = 'https://slack.com/api/oauth.access'
`

5. Use the url to authenticate your users in your templates

`<a href='{% url 'slack_auth' %}'>Get slacked</a>`

6. Find your token in `slack_user` table

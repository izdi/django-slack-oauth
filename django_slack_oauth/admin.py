from django.contrib import admin

from django_slack_oauth.models import SlackOAuthRequest


@admin.register(SlackOAuthRequest)
class SlackOAuthAdmin(admin.ModelAdmin):
    pass

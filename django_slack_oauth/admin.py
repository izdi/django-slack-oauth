# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import SlackOAuthRequest


@admin.register(SlackOAuthRequest)
class SlackOAuthAdmin(admin.ModelAdmin):
    pass

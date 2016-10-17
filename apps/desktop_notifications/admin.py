# -*- coding: utf-8 -*-


from django.contrib import admin

from models import Notification

class NotificationAdmin(admin.ModelAdmin):
    readonly_fields=('sended_at',)
admin.site.register(Notification, NotificationAdmin )
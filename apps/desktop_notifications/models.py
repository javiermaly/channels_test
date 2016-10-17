# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver

from django.utils.translation import ugettext_lazy as _

from knocker.mixins import KnockerModel
from knocker.signals import notify_items, active_knocks
from meta.models import ModelMeta

class Notification(KnockerModel, ModelMeta, models.Model):
    message = models.CharField(_('Texto Notificación'), max_length=255)
    sended_at = models.DateTimeField(_('Fecha Notificación'),
                                          default=timezone.now)

    _knocker_data = {
        'title': 'get_title',
        'message': 'get_message',
        'icon': 'https://cdn2.iconfinder.com/data/icons/mixed-rounded-flat-icon/512/rocket-128.png',
        'url': 'http://localhost:8000',
        'language': 'en-us',
    }

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.message

    def get_title(self):
        return 'Notificación desde XXXX'

    def get_message(self):
        return self.message


    class Meta:
        verbose_name = _('Notificación')
        verbose_name_plural = _('Notificaciones')

@receiver(post_save, sender=Notification)
def notify(sender, instance, **kwargs):
    print 'estoy'
    instance.send_knock(True)






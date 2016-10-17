# -*- coding: utf-8 -*-
from channels import include
from knocker.routing import channel_routing as knocker_routing


channel_routing = [
    include(knocker_routing, path=r'^/notifications'),
]
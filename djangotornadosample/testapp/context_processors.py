# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import get_current_site


def websocket_port(request):
    return {
        'WS_PORT': settings.TORNADO_WS_PORT,
        'CURRENT_SITE': get_current_site(request),
    }
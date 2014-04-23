# -*- coding: utf-8 -*-
import time
import random

import zmq

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        context = zmq.Context()
        publisher = context.socket(zmq.PUB)
        publisher.bind("tcp://127.0.0.1:%d" % settings.AGENT_TO_DJANGO_PORT)

        while True:
            value = random.randint(1, 100)
            print value
            publisher.send("django:%d" % value)
            time.sleep(1)

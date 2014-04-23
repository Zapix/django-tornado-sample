# -*- coding: utf-8 -*-
import time
import signal

import zmq
from zmq.eventloop import ioloop
from zmq.eventloop import zmqstream
from tornado import httpserver

from django.conf import settings
from django.core.management import base as base_management

from testapp.tornadoapp import application
from testapp.tornadoapp import handle_message_from_agent

ioloop.install()


class Command(base_management.BaseCommand):
    help = "Starts tornado server on port"
    http_server = None

    def sig_handler(self, sig, frame):
        """Catch signal and init callback"""
        ioloop.IOLoop.instance().add_callback(self.shutdown)

    def shutdown(self):
        self.http_server.stop()
        io_loop = ioloop.IOLoop.instance()
        io_loop.add_timeout(time.time() + 2, io_loop.stop)

    def handle(self, *args, **kwargs):
        port = settings.TORNADO_WS_PORT

        self.http_server = httpserver.HTTPServer(application)
        self.http_server.listen(port, '0.0.0.0')

        signal.signal(signal.SIGTERM, self.sig_handler)
        signal.signal(signal.SIGINT, self.sig_handler)

        context = zmq.Context()
        subscriber = context.socket(zmq.SUB)
        subscriber.connect(
            'tcp://127.0.0.1:%d' % settings.AGENT_TO_DJANGO_PORT
        )
        subscriber.setsockopt(zmq.SUBSCRIBE, 'django')
        stream = zmqstream.ZMQStream(subscriber)
        stream.on_recv(handle_message_from_agent)

        ioloop.IOLoop.instance().start()
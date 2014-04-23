# -*- coding: utf-8 -*-
import json

from tornado import web
from tornado import websocket

connected_clients = []


class MainHandler(web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("Main")


class SampleWsHandler(websocket.WebSocketHandler):

    def open(self):
        print "Client connected"
        connected_clients.append(self)

    def on_close(self):
        print "Client disconnected"
        connected_clients.remove(self)


def handle_message_from_agent(messages):
    for message in messages:
        for client in connected_clients:
            client.write_message(json.dumps({"message": message.split(':')[1]}))


application = web.Application([
    (r'/', MainHandler),
    (r'/ws/', SampleWsHandler)
])

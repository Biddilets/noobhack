import re

import dungeun
import status 

class Dispatcher:
    def __init__(self):
        self.listeners = {}

    def add_event_listener(self, event, function):
        if not self.listeners.has_key(event):
            self.listeners[event] = []

        self.listeners[event].append(function)

    def remove_event_listener(self, event, function):
        pass

    def dispatch(self, event, **kwargs):
        for l in self.listeners.get(event, []):
            l(event, kwargs)

    def _dispatch_status_event(self, name, value):
        self.dispatch("status", name=name, value=value)

    def _dispatch_dungeon_event(self, name):
        self.dispatch("dungeon", name=name)

    def process(self, data):
        for name, messages in dungeon.messages.iteritems():
            for message in messages:
                match = re.search(message, data, re.I | re.M)
                if match is not None:
                    self._dispatch_dungeon_event(name)

        for name, messages in status.messages.iteritems():
            for message, value in messages.iteritems():
                match = re.search(message, data, re.I | re.M)
                if match is not None:
                    self._dispatch_status_event(name, value)

dispatcher = Dispatcher()

import os
from pulsar.apps import wsgi

__all__ = ['WsgiMeta', 'PulsarApp']


class WsgiMeta(type):
    def __call__(cls, *args, **kwargs):
        return super(WsgiMeta, cls).__call__(*args, **kwargs)


class PulsarApp(wsgi.LazyWsgi, metaclass=WsgiMeta):
    def __init__(self, app=None, middleware=None):
        self.application = app
        self.middleware = middleware
        return super(PulsarApp, self).__init__()

    def getapp(self):
        module = __import__(self.application)
        return getattr(module, 'application', getattr(module, 'app', module))

    def getmiddlemare(self):
        if not self.middleware:
            return []
        module = __import__(self.middleware)
        return getattr(module, 'middleware', getattr(module, 'mdw', module))

    def setup(self, environ=os.environ):
        app = self.getapp()
        middlewares = [
            wsgi.wait_for_body_middleware,
            wsgi.middleware_in_executor(app)] + self.getmiddlemare()
        return wsgi.WsgiHandler(tuple(middlewares))

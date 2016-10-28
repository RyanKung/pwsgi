from pulsar.apps import wsgi

__all__ = ['wrap2pwsgi']

def wrap2pwsgi(application):
    '''
    Wrap a wsgi app to pwsgi app
    '''

    class PulsarApp(wsgi.LazyWsgi):
        def setup(self, environ=None):
            app = application
            return wsgi.WsgiHandler((wsgi.wait_for_body_middleware,
                                     wsgi.middleware_in_executor(app)))

    return PulsarApp

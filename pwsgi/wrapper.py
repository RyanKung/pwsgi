from pulsar.apps import wsgi

__all__ = ['wrap2pwsgi', 'PulsarApp']


class PulsarApp(wsgi.LazyWsgi):
    pass


def wrap2pwsgi(application):
    '''
    Wrap a wsgi app to pwsgi app
    '''
    def setup_fn(application):
        def setup(self, environ=None):
            app = application
            return wsgi.WsgiHandler((wsgi.wait_for_body_middleware,
                                     wsgi.middleware_in_executor(app)))
        return
    return type('PulsarApp', (wsgi.LazyWsgi, ), {'setup': setup_fn(application)})

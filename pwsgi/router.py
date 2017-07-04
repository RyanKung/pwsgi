__all__ = ['router']


def router(app, rule, method):
    '''Map a function to :class:`Router` and add to the :attr:`routes` list.
    Typical usage:

    app = WsgiApplication('/')

    @app.router('/hello', method='post')
    def world(request):
        return wsgi.WsgiResponse(200, 'world')
    '''
    def handler(fn):
        app.add_child(app.make_router(rule, method, fn))
        return fn
    return handler

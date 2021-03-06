from functools import partial
from typing import Iterable
from pulsar.apps.wsgi import Router


__all__ = ['router']


def router(parent: Router, rule: str, methods: Iterable):
    '''Map a function to :class:`Router` and add to the :attr:`routes` list.
    Typical usage:

    app = WsgiApplication('/')

    @app.router('/hello', methods=['post', 'get'])
    def world(request):
        return wsgi.WsgiResponse(200, 'world')
    '''
    def handler(fn):
        for method in methods:
            parent.add_child(
                parent.make_router(rule, method.lower(), fn))
        return fn
    return handler


class BluePrint(Router):
    '''
    To patch pulsar.wsgi, if it dosent have `router` decorator
    '''

    def __init__(self, *args, **kwargs) -> None:
        if not hasattr(Router, 'router'):
            self.router = partial(router, self)
            # the classmethod fn is actually `partial(self, fn)`
        super().__init__(*args, **kwargs)

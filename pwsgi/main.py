from argparse import ArgumentParser
from pwsgi import __version__
import os
import sys
from pulsar.apps import wsgi
from pwsgi.wrapper import wrap2pwsgi

parser = ArgumentParser(add_help=False, description='pWsgi - a pulsar based async wsgi implentation %s' % __version__)
parser.usage = 'pwsgi [-h]'
parser.add_argument('-a', '--app', help='path of wsgi app, required')
parser.add_argument('-w', '--work_path', help='work path of wsgi app [default: ./wsgiapp.py]', default='./')

args, tails = parser.parse_known_args()
os.chdir(args.work_path)
sys.path.append('.')


def load_wsgi(app):
    wsgi_app = __import__(app).application
    return wrap2pwsgi(wsgi_app)


def main(**kwargs):
    if len(sys.argv) == 1 or '-h' in tails:
        print(parser.format_help())
        print('-----------------------------')
    sys.argv = [sys.argv[0]] + tails
    if args.app:
        return wsgi.WSGIServer(load_wsgi(args.app)(), **kwargs).start()


if __name__ == '__main__':
    try:
        main()
    except InterruptedError:
        exit(1)

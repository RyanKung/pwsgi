# TL;DR

`pWSGI` is a WSGI wrapper with `pulsar`. It can easily map a wsgi app (such as
`Flask app` or `djang app`) to a `pulsar wsgi app` with full features supporting by `pulsar`.

# How To Use

* Basic

```
usage: pwsgi [-h]

pWsgi - a pulsar based async wsgi implentation 0.1

optional arguments:
  -a APP, --app APP     path of wsgi app, required
  -w WORK_PATH, --work_path WORK_PATH
                        work path of wsgi app [default: ./wsgiapp.py]

```
* Run as pulsar wsgi

```

(shadowfax) ➜  thunder-dev pwsgi -a wsgiapp -w ./shadowfax -h
usage: pwsgi [-h]

pWsgi - a pulsar based async wsgi implentation 0.1

optional arguments:
  -a APP, --app APP     path of wsgi app, required
  -w WORK_PATH, --work_path WORK_PATH
                        work path of wsgi app [default: ./wsgiapp.py]

usage: pwsgi [-h] [--version] [-c FILE] [--http-proxy HTTP_PROXY]
             [--http-keep-alive HTTP_KEEP_ALIVE] [--debug] [-D] [--reload]
             [-p FILE] [--password PASSWORD] [-u USER] [-g GROUP]
             [--log-level LOG_LEVEL [LOG_LEVEL ...]]
             [--log-handlers LOG_HANDLERS [LOG_HANDLERS ...]] [-n STRING]
             [--coverage] [--data-store CONNECTION STRING] [--exc-id EXC_ID]
             [--io {kqueue,poll,select,uv}] [--redis-py-parser]
             [--redis-server CONNECTION_STRING] [-b ADDRESS]
             [--keep-alive KEEP_ALIVE] [--backlog BACKLOG] [--key-file FILE]
             [--cert-file FILE] [-w WORKERS]
             [--concurrency {process,thread,coroutine,multi}]
             [--max-requests MAX_REQUESTS] [-t TIMEOUT]
             [--thread-workers THREAD_WORKERS]

Pulsar server

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -c FILE, --config FILE
                        The path to a Pulsar config file, where default
                        Settings parameters can be specified. [config.py]
  --http-proxy HTTP_PROXY
                        The HTTP proxy server to use with HttpClient. []
  --http-keep-alive HTTP_KEEP_ALIVE
                        Keep HTTP connections alive for this number of seconds
                        [15]
  --debug               Turn on debugging. [False]
  -D, --daemon          Daemonize the pulsar process (posix only). [False]
  --reload              Auto reload modules when changes occurs. [False]
  -p FILE, --pid-file FILE
                        A filename to use for the PID file. [None]
  --password PASSWORD   Set a password for the server [None]
  -u USER, --user USER  Switch worker processes to run as this user. [None]
  -g GROUP, --group GROUP
                        Switch worker process to run as this group. [None]
  --log-level LOG_LEVEL [LOG_LEVEL ...]
                        The granularity of log outputs. [['info']]
  --log-handlers LOG_HANDLERS [LOG_HANDLERS ...]
                        Log handlers for pulsar server [['console']]
  -n STRING, --process-name STRING
                        A base to use with setproctitle for process naming.
                        [None]
  --coverage            Collect code coverage from all spawn actors. [False]
  --data-store CONNECTION STRING
                        Default data store. []
  --exc-id EXC_ID       Execution ID. []
  --io {kqueue,poll,select,uv}
                        Specify the event loop used for I/O event polling.
                        [kqueue]
  --redis-py-parser     Use the python redis parser rather the C
                        implementation. [False]
  --redis-server CONNECTION_STRING
                        Default connection string for the redis server
                        [127.0.0.1:6379/7]
  -b ADDRESS, --bind ADDRESS
                        The socket to bind. [127.0.0.1:8060]
  --keep-alive KEEP_ALIVE
                        The number of seconds to keep an idle client
                        connection open. [15]
  --backlog BACKLOG     The maximum number of queued connections in a socket.
                        [2048]
  --key-file FILE       SSL key file [None]
  --cert-file FILE      SSL certificate file [None]
  -w WORKERS, --workers WORKERS
                        The number of workers for handling requests. [1]
  --concurrency {process,thread,coroutine,multi}
                        The type of concurrency to use. [process]
  --max-requests MAX_REQUESTS
                        The maximum number of requests a worker will process
                        before restarting. [0]
  -t TIMEOUT, --timeout TIMEOUT
                        Workers silent for more than this many seconds are
                        killed and restarted. [30]
  --thread-workers THREAD_WORKERS
                        Maximum number of threads used by the actor event loop
                        executor. [5]

Have fun!

```

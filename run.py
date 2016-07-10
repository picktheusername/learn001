#!/usr/bin/env python
# coding=utf-8

"""Basic run script"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
from tornado.options import options
import tornado.web

from settings import settings
from urls import url_patterns


class TornadoApplication(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    print(options.port)
    app = TornadoApplication()
    app.listen(options.port, address='127.0.0.1')
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

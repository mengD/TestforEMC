
import os
import sys
import logging

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver

from tornado.httpclient import AsyncHTTPClient
from tornado.options import define, options

from StorageHandler import CreateLUN
from StorageHandler import ListLUN
from StorageHandler import ModifyLUN
from StorageHandler import DeleteLUN
from Storage import Storage

define("port", default=8888, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()

    #AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient", max_clients=2000)

    storage = Storage()

    settings = {
        'debug': True,
        'autoreload': True,
        'storage': storage,
    }

    app = tornado.web.Application([
        (r"/api/lun/create", CreateLUN),
        (r"/api/lun/list", ListLUN),
        (r"/api/lun/modify", ModifyLUN),
        (r"/api/lun/delete",DeleteLUN)
    ],**settings)

    ioloop = tornado.ioloop.IOLoop.current()
    app.listen(options.port)
    ioloop.start()

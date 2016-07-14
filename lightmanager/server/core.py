"""
Core module of the lighting system

The core module loads all dependent modules and runs the whole package.

Author: Leonard de Vries
Created: 12-07-2016
"""
import logging
import time
import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.websocket

import common.log

common.log.setup_logging()
logger = logging.getLogger(__name__)


class LightManagerServer:
    def __init__(self):
        pass

    def run(self):
        while True:
            time.sleep(10)


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message("Hello World")

    def on_message(self, message):
        print 'message received %s' % message

    def on_close(self):
        print 'connection closed'


def run():
    logger.info("running server..")
    application = tornado.web.Application([
        (r'/ws', WSHandler),
    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run()

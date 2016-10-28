"""
Core module of the lighting system

The core module loads all dependent modules and runs the whole package.

Author: Leonard de Vries
Created: 12-07-2016
"""
import json
import logging
import time
import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.websocket

import common.log

common.log.setup_logging()
logger = logging.getLogger("core")

accepted_tokens = ["flb9asd0f9aop9b9a8sd6b986eb9879cd898b"]


class LightManagerServer:
    def __init__(self):
        pass

    def run(self):
        while True:
            time.sleep(10)


class WSHandler(tornado.websocket.WebSocketHandler):
    authenticated = False

    def check_origin(self, origin):
        return True

    def open(self):
        logger.info("New connection accepted")
        self.write_message(json.dumps("AUTH"))

    def on_message(self, message):
        if not self.authenticated:
            if str(message).startswith("KEY:"):
                if str(message).split(":")[1] in accepted_tokens:
                    self.authenticated = True
                    logger.info("Client successfully authenticated!")
                    self.write_message("AUTH_OK")
                else:
                    logger.warning("Client denied on key")
            else:
                logger.warning("Received message while not authenticated!")
                self.close(code=4000, reason="Unauthorized")
        else:
            logger.debug('message received %s' % message)

    def on_close(self):
        logger.info('connection closed')


def run():
    logger.info("running server..")
    application = tornado.web.Application([
        (r'/ws', WSHandler),
    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    http_server.xheaders = True
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run()

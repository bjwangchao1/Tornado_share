import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8010, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world!")


if __name__ == '__main__':
    tornado.options.parse_command_line()

    application = tornado.web.Application([(r"/", MainHandler), ], autoreload=True)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()

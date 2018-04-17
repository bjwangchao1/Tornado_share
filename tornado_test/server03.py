import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8000)
    httpServer.bind(8000)
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

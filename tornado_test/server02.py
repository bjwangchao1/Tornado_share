import tornado.web
import tornado.ioloop
# 引入httpserver模块
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("ccx is a good company")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    # app.listen(8000)
    # 实例化一个http服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    httpServer.listen(8000)

    tornado.ioloop.IOLoop.current().start()

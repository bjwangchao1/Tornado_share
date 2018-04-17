import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    """
    主路由处理类
    """

    def get(self):
        """
        对应http的get请求方式
        :return:
        """
        self.write("Hello ccx!")


if __name__ == '__main__':
    app = tornado.web.Application([(r'/', IndexHandler)])
    # -----------------------------------
    http_sever = tornado.httpserver.HTTPServer(app)
    http_sever.listen(8000)
    # ------------------------------------
    tornado.ioloop.IOLoop.current().start()

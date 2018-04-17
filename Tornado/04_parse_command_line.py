import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8000, type=int, help="run server on the given port")
tornado.options.define("itcast", default=[], type=str, multiple=True, help="itcast subjects")


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("Hello ccx1!")


if __name__ == "__main__":
    # tornado.options.parse_command_line()
    tornado.options.parse_config_file("./config")
    print(tornado.options.options.itcast)  # 输出多值选项
    app = tornado.web.Application([(r"/", IndexHandler), ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

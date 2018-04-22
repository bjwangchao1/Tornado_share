import tornado.web
import tornado.ioloop
# 引入httpserver模块
import tornado.httpserver

import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # greet = self.get_query_argument('a')
        # self.write(greet + ",welcome to ccx!")

        greet = self.get_query_arguments('a')
        # self.write(greet + ",welcome to ccx!")
        print(greet)
        self.write('ok')


class IndexHandler2(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('ok!')

        stu = {
            "name": "liyingkun",
            "age": 22,
            "gender": 1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # self.set_status(404)
        # self.send_error(404, content="出现404错误")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/ccx/([a-z]+)", IndexHandler2)
    ])
    # app.listen(8000)
    # 实例化一个http服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    httpServer.listen(8000)

    tornado.ioloop.IOLoop.current().start()

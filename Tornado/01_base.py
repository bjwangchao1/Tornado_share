import tornado.web
import tornado.ioloop
import json
import tornado.httpserver
import tornado.options


#  类比Django中的识图
#  一个业务处理类
class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""

    def set_default_headers(self):
        print("set_default_header")
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header("Itcast", "Python")

    def write_error(self, status_code, **kwargs):
        """
        error_title=错误标题
        error_content=错误描述

        :param status_code:
        :param kwargs:
        :return:
        """
        self.write("出错了<br/>")
        self.write("标题:%s<br/>" % kwargs.get("err_title", ""))
        self.write("详情:%s<br/>" % kwargs.get("err_content", ""))

    # 处理get请求，不能处理post请求
    def get(self):
        # 对应http请求的方法，给浏览器响应信息
        # self.write("hello ccx<br/>")
        # self.write("wangchao_ccx<br/>")
        # self.write("shanxi_baoji")
        stu = {
            "name": "wangchaos",
            "age": 25,
            "gender": 1,
        }
        stu_json = json.dumps(stu)
        error_data = {
            "err_content": "abc",
            "err_title": "title"
        }
        self.send_error(404, **error_data)
        self.write(stu_json)
        # self.set_header("Content-Type", "application/json;charset=UTF-8")
        self.set_header("Itcast", "CPP")
        self.set_status(444, "ccx error")

    def post(self):
        print("run post")
        stu = {
            "name": "zhangsan",
            "age": 24,
            "gender": 1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)


if __name__ == '__main__':
    # 实例化一个app应用对象
    # Application：是tornado web框架的核心应用类，是与服务器对应的接口
    # 里面保存了路由映射表，listen方法用来创建一个http服务器的实例，并绑定了端口
    app = tornado.web.Application([(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    # 绑定监听端口
    # 注意：此时的服务器并没有开启监听
    # app.listen(8000)
    """
    IOLoop.current()：返回当前线程的IOLoop实例
    IOLoop.start():启动IOLoop实例的I/O循环，同时开启了监听

    """
    tornado.ioloop.IOLoop.current().start()

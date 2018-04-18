import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("ccx is a good company")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8000)
    httpServer.bind(8000)
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
    """
    虽然tornado给我们提供了一次开启多个进程的方法，但是由于：

    每个子进程都会从父进程中复制一份IOLoop实例，如过在创建子进程前我们的代码动了IOLoop实例，那么会影响到每一个子进程，势必会干扰到子进程IOLoop的工作；
    所有进程是由一个命令一次开启的，也就无法做到在不停服务的情况下更新代码；
    所有进程共享同一个端口，想要分别单独监控每一个进程就很困难。
    不建议使用这种多进程的方式，而是手动开启多个进程，并且绑定不同的端口。
    """

import time
import threading


def genCoroutine(func):
    def wrapper(*args, **kwargs):
        gen1 = func()  # reqA的生成器
        gen2 = next(gen1)  # longIo的生成器

        def run(g):
            res = next(g)  # res 就是 ccx is a good company
            try:
                gen1.send(res)  # 返回给reqA数据
            except StopIteration as e:
                pass

        threading.Thread(target=run, args=(gen2,)).start()

    return wrapper


# handler获取数据(数据库、其他服务器、循环耗时)
def long_io():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")
    # 返回数据
    yield "ccx is a good company"


# 一个客户单的请求
@genCoroutine
def req_a():
    print("开始处理reqA")
    res = yield long_io()
    print("接收到longIo的响应数据：", res)
    print("结束处理reqA")


# 另一个客户端的请求
def req_b():
    print("开始处理reqB")
    time.sleep(2)
    print("结束处理reqB")


# tornado服务
def main():
    req_a()
    req_b()
    while 1:
        time.sleep(0.1)
        pass


if __name__ == "__main__":
    main()

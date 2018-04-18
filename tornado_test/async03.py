import time
import threading

gen = None


# handler获取数据(数据库、其他服务器、循环耗时)
def long_io():
    def run():
        print("开始耗时操作")
        time.sleep(5)
        try:
            global gen
            gen.send("ccx is a good company")
        except StopIteration as e:
            pass

    threading.Thread(target=run).start()


def genCoroutine(func):
    def wrapper(*args, **kwargs):
        global gen
        gen = func()
        next(gen)

    return wrapper


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
    # global gen
    # gen = reqA()#生成一个生成器
    # next(gen)#执行reqA
    req_a()
    req_b()
    while 1:
        time.sleep(0.1)
        pass


if __name__ == "__main__":
    main()

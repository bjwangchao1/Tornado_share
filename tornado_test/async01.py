import time
import threading


# handler获取数据(数据库、其他服务器、循环耗时)
def long_io(callback):
    def run(cb):
        print("开始耗时操作")
        time.sleep(5)
        print("结束耗时操作")
        cb("ccx is a good company")

    threading.Thread(target=run, args=(callback,)).start()


# 函数(回调函数)
def finish(data):
    print("开始处理回调函数")
    print("接收到longIo的响应数据：", data)
    print("结束处理回调函数")


# 一个客户端的请求
def req_a():
    print("开始处理reqA")
    long_io(finish)
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

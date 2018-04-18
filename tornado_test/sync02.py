import time


# handler获取数据(数据库、其他服务器、循环耗时)
def long_io():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")
    return "ccx is a good company"


# 一个客户单的请求
def req_a():
    print("开始处理reqA")
    res = long_io()
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

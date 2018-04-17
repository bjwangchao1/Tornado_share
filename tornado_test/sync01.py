import time


# 一个客户单的请求
def reqA():
    print("开始处理reqA")
    print("结束处理reqA")


# 另一个客户端的请求
def reqB():
    print("开始处理reqB")
    print("结束处理reqB")


# tornado服务
def main():
    reqA()
    reqB()
    while 1:
        time.sleep(0.1)
        pass


if __name__ == "__main__":
    main()

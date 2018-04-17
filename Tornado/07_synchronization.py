import time


def long_io():
    """模拟耗时IO操作"""
    print("开始执行IO操作")
    time.sleep(5)
    print("完成IO操作")
    return "io result"


def req_a():
    print("开始处理请求req_a")
    ret = long_io()
    print("ret: %s" % ret)
    print("完成处理请求req_a")


def req_b():
    print("开始处理请求req_b")
    print("完成处理请求req_b")


def main():
    req_a()
    req_b()


if __name__ == "__main__":
    main()

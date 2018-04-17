import time
import _thread


def long_io():
    print('开始执行耗时操作')
    time.sleep(5)
    print('完成执行耗时操作')
    yield 'io_result'


def gen_coroutine(func):
    def wrapper():
        gen_f = func()
        r = gen_f.__next__()

        def fun(g):
            ret = g.__next__()
            try:
                gen_f.send(ret)
            except StopIteration:
                pass

        _thread.start_new_thread(fun, (r,))

    return wrapper


@gen_coroutine
def req_a():
    print('开始处理请求a')
    ret = yield long_io()
    print(ret)
    print('完成处理请求a')


def req_b():
    print('开始处理请求b')
    time.sleep(2)
    print('完成处理请求b')


def main():
    req_a()
    req_b()
    while 1:
        pass


if __name__ == '__main__':
    main()

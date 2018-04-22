import time


def test(number):
    print('---1---')

    def test_in(number2):
        print('---2---')
        print(number + number2)

    print('---3---')
    return test_in

@timeit
def f1():
    print('---f1---')


def timeit(func):
    """
    装饰器，计算函数执行时间
    """

    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        exec_time = time_end - time_start
        print('{function} exec time: {time}s'.format(function=func.__name__, time=exec_time))
        return result

    return wrapper


if __name__ == '__main__':
    # ret = test(100)
    # print('-' * 30)
    # ret(1)
    # ret(100)
    f1 = timeit(f1)
    f1()

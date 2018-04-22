# 斐波那契数列
def create_num():
    print("-----start----")
    a, b = 0, 1
    for i in range(5):
        print('---1---')
        yield b
        print('---2---')
        a, b = b, a + b
        print('---3---')
    print('---stop---')



def test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1





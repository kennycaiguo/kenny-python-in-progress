def demo():  # 函数名称是函数的一个引用
    for i in range(5):
        for j in range(i + 1):
            print("*", end='')
        print()


def demo2():
    print("demo2")


def call_func(fun):
    print("calling function {}".format(demo))
    fun()


def double_up(lst):
    return [i * 2 for i in lst]


def map_func(fun, lst):
    return fun(lst)


if __name__ == '__main__':
    # demo2()  # 输出demo2
    # demo2 = demo  # 将demo2指向domo指向的地址，demo2将会指向demo的代码
    # demo2()  # 执行demo的代码输出5行*
    call_func(demo)  # 函数可以作为参数传递给另外一个函数

    lst = [1, 2, 3, 4, 5]
    lst = map_func(double_up, lst)
    print(lst)

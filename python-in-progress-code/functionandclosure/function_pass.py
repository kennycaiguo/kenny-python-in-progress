def demo():  # 函数名称是函数的一个引用
    for i in range(5):
        for j in range(i + 1):
            print("*", end='')
        print()


if __name__ == '__main__':
    a = demo   # 函数名称就是一个地址，可以用一个变量指向这个地址，那么就有两个变量指向这个函数的地址，如果删除一个另外一个函数可以找到函数的地址因此函数可以正常执行
    print(id(a) == id(demo))  # True,说明他们都指向同一个地址
    del demo  # 注意！！！，python的delete操作删除的是变量，而c++的delete操作删除的是变量指向的内存，所以在python中一定要保证还有其他变量引用该内存你才可以删除这个变量，否则内存泄露
    a()

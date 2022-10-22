def outer():  # 嵌套函数必须就内层函数返回，否则外部无法使用
    x = 100
    print('this is outer func')
    print(x)

    def inner():
        nonlocal x
        x = 100
        print('this is inner')
        print(x)

    return inner


fun = outer()  # 嵌套函数的正确使用步骤1，使用引发变量接收外出函数的返回值，那么外层函数的代码也执行了

fun()  # 调用内层函数

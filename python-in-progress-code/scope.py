import builtins

# print(dir(builtins))
'''
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问，如下代码：
'''

if True:
    msg = "That is right!!!"
print(msg)  # 在if语句里面定义的变量。在if外面是可以使用的，因为if语句不会产生作用域

a = 5

'''
global关键字可以将一个局部变量提升为全局变量，如果外部有一个同名的变量就覆盖，没有就创建
nonlocal 关键字可以将嵌套函数内层的变量的作用域提升为外层函数的作用域，作用和global类似
但是global 和 nonlocal 关键字不能作用到同一个变量名称中会有冲突
'''

def test_func():
    global a  # 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。前提是局部变量和全局变量名字相同
    a = 100
    print(a)


test_func()
print(a)

print("=====================================")


# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
# 对比下面两个嵌套函数
def outer_func():
    num = 100

    def inner_func():
        num = 1000
        print("inside inner:num=", num)

    inner_func()
    print('outside inner:num=', num)


outer_func()

print("==============================")


def outer():
    number = 100

    def inner():
        nonlocal number
        number = 1000
        print("inside inner:num=", number)

    inner()
    print('outside inner:num=', number)


outer()

# 下面的写法是错误的，因为此时局部变量a还没有创建，不能修改
# a = 10
# def test():
#     a = a+1
#     print(a)
# test()

a = 10


def test():
    global a
    a = a + 1
    print(a)


test()

# 也可以通过函数参数传递：

b = 10


def test2(b):
    b = b + 1
    print(b)


test2(b)


# 可以在函数里面声明一个全局变量供外部使用
def local_to_global():
    global v
    v = 100
    print('v=', v)


local_to_global()
print(v)

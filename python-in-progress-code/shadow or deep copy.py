"""
python中的深拷贝和浅拷贝
可变和不可变对象
在python中有6个标准数据类型，他们分为可变和不可变两类。

不可变类型：Number（数字）String（字符串）Tuple（元组）
可变类型：List（列表）Dictionary（字典）Set（集合）
可变对象和不可变对象的内存地址可以通过id函数获取

可变对象：可变对象可以在其 id() 保持固定的情况下改变其取值；
不可变对象：具有固定值的对象。不可变对象包括数字、字符串和元组。这样的对象不能被改变。如果必须存储一个不同的值，则必须创建新的对象。
id(object)： 函数用于获取对象的内存地址，函数返回对象的唯一标识符，标识符是一个整数。
字符串和数字都是不可变类型，不同变量赋值一样，通过id获取的内存地址是一样的
元组只能用深拷贝，不能使用浅拷贝
"""
import copy

def demo1():  # 字符串和数字都是不可变类型，不同变量赋值一样，通过id获取的内存地址是一样的
    a = "abc"
    b = "abc"
    print(id(a), id(b))
    print(a is b)


def demo2():  # list、dict 和 set集合是可变类型，虽然值一样，但是id获取的内存地址不一样
    a = {'key': 123}
    b = {'key': 123}
    print(id(a), id(b))  # id() 不一样
    print(a is b)  # 不是同一个对象
    print(a == b)  # 他们的值相等
    print("------------------------------------")
    c = [1, 2, 3]
    d = [1, 2, 3]
    print(id(c))
    print(id(d))
    print(c is d)
    print(c == d)


def shadow_copy():
    # 浅拷贝使用 copy 模块的 copy 方法

    a = [1, "hello", [2, 3], {"key": "123"}]
    b = copy.copy(a)
    print(id(a))    # 外面容器拷贝了，所以a和b的id不一样
    print(id(b))

    # a和b容器里面的元素对象id
    print(id(a[2]))   # 这两个的id是一样的
    print(id(b[2]))
    '''
    浅拷贝是拷贝了list外面一层的， 创建一个新的容器对象(compound object)，所以a和b的id是不一样的
    对于容器里面的元素对象，浅拷贝就只会使用原始元素的引用（内存地址），所以可以看到子元素的内存地址还是一样的
    '''


def deep_copy():
    a = [1, "hello", [2, 3], {"key": "123"}]
    b = copy.deepcopy(a)
    print(id(a),id(b))  # 1641865374216 1641865374088 地址不一样
    print(a is b)  # false
    b[1] = "Girls"
    print(b)
    print(a)  # 对b的任何操作都不会影响a



if __name__ == '__main__':
    # demo1()
    # demo2()
    # shadow_copy()
    deep_copy()

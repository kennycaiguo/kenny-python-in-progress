from functools import reduce

"""
python中4个常用的内置高阶函数:map,reduce,sorted,filter,sum()，
map可以接收只需要一个参数的函数和一个可迭代对象序列如：列表，它将安装函数的规则依次作用与序列的每一个元素，返回一个可迭代对象需要转换为对于的序列如：列表
reduce函数接收一个函数和一个序列，传递给它的函数必须接收两个参数，它会累计
Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是
丢弃该元素。返回一个可迭代对象需要转换为对于的序列如：列表
sorted
排序算法
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

Python内置的sorted()函数就可以对list进行排序：
"""


# reduce
def plus(x, y):  # reduce函数，会累计调用，传递给它的函数必须接收两个参数
    return x + y


def mul(a, b):
    return a * b


def test_reduce():
    r = reduce(plus, [1, 2, 3, 4, 5])
    print(r)
    print("=============================")
    a = reduce(mul, [1, 2, 3, 4, 5])  # 1*2*3*4*5
    print(a)


def test_reduce_lambda():
    r = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # reduce 元素可以传递lambda表达式的
    print(r)  # 15


def map_test():
    lst = [1, 2, 3, 4, 5]
    print(list(map(lambda x: x ** 2, lst)))  # [1, 4, 9, 16, 25] 函数可以传递lambda表达式


def map_test2():
    lst = [1, 2, 3, 4, 5]
    print(list(map(str, lst)))  # ['1', '2', '3', '4', '5']将列表的每一个元素都转为字符


def filter_test():
    res = filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(res))  # [1, 3, 5, 7, 9]


def filter_test2():
    """把一个序列中的空字符串删掉，可以这么写："""
    str_list = ['a', 'b', '', None, 'c']
    res = filter(lambda x: x and x.strip(), str_list)
    print(list(res))


def sorted_test1():
    print(sorted([36, 5, -12, 9, -21]))  # [-21, -12, 5, 9, 36]


def sorted_test2():
    print(sorted([36, 5, -12, 9, -21], key=abs))  # 根据绝对值来排序 [5, 9, -12, -21, 36]


def sorted_test3():
    print(sorted(['bob', 'about', 'Zoo', 'Credit']))  # ['Credit', 'Zoo', 'about', 'bob'] 大写字母的ascii码比小写字母的ASCII码小


def sorted_test4():
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))  # 按照小写字母排序


def sorted_test5():
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  # 按照小写字母排序倒序排列


'''
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
'''


def lazy_sum(lst):
    def my_sum():
        total = 0
        for i in lst:
            total += i
        return total

    return my_sum


if __name__ == '__main__':
    # test_reduce()
    # test_reduce_lambda()
    # map_test()
    # map_test2()
    # filter_test()
    # filter_test2()
    # sorted_test1()
    # sorted_test2()
    # sorted_test3()
    # sorted_test4()
    # sorted_test5()
    f = lazy_sum([1, 2, 3, 4, 5])
    print(f())  # 也可以这么写print(lazy_sum([1, 2, 3, 4, 5])())

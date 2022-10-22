"""
python中的容器主要有list，tuple，dict，set
list的特点是运算可以重复，类型可变
tuple是可以重复，类型不可变，内容可变，也就是说如果元组里面有列表成员，列表的成员可变
dict：key：value键值对，key必须是唯一，值可以重复，是无序的，可以实现快速查找
set的特点是不重复，如果菜单重复数据它会自动去重
"""



def demo1():
    l = [1, 1, 2, 2, 3, 3]
    print(l)
    print("================================")
    t = (1, 1, 2, 2, 3, 3, l)  # 一般来说元组的元素的值不能改变，但是如果列表是元组是元素，则列表可以修改
    print(t)
    # t[5] = 6 错误，元组的元素不能赋值
    l.append(100)
    print(t[6])
    print(t)  # (1, 1, 2, 2, 3, 3, [1, 1, 2, 2, 3, 3, 100])
    print("================================")
    d = {('a,', 'b'): 100}
    print(d)

    # d2 = {['a','b']:100}  # 报错，因为key是不可变的，你菜单的列表是可变的，就好抛异常
    s = set(l)
    print(s)  # {1, 2, 3, 100}
    print("================================")
    dic = {"name": 'jack', 'age': 30, 'nickname': 'j1'}
    dic2 = {"name": 'jack', 'age': 20, 'nickname': 'j1'}

    s2 = set(dic2)  # 将字典转换位set没有多大意义，因为只有key，没有value
    print(s2)


def set_demo():
    # set集合基本操作（添加、删除、交集、并集、差集）
    s1 = set([1, 2, 3, 4, 5])
    s2 = set([4, 5, 6, 7, 8])

    # 添加元素add方法
    # 需要注意的是，使用 add() 方法添加的元素，只能是数字、字符串、元组或者布尔类型（True 和 False）值，不能添加列表、字典、集合这类可变的数据
    s1.add(9)
    s2.add(9)
    # print(s1)
    # print(s2)
    # 删除元素remove方法
    # 需要注意的是，如果被删除元素本就不包含在集合中，则此方法会抛出 KeyError 错误
    # 还有一个discard方法，也可以删除元素的但是它不会抛异常
    # s1.remove(9)
    # s1.discard(9)
    # print(s1)
    # 交集
    s = s1.intersection(s2)
    print(s)  # {4, 5}
    # 并集 union
    s_u = s1.union(s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(s_u)
    # 差集 difference
    print(s1.difference(s2))


def set_travel():  # set集合的遍历，注意python中set也是可以遍历的！！！
    # 第一种方式：内置函数iter（），返回一个迭代器对象
    girl_set = set(["美女", "好看的美女", "特别好看的美女"])
    for g in iter(girl_set):  # 仍然是无序的
        print(g, end=',')
    print('')
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # 第二种方式：for in
    for gr in girl_set:
        print(gr, end=',')
    print('')
    print('==============================================')

    # 第三种方式：内置函数enumerate(）
    for i, v in enumerate(girl_set):
        print(str(i) + ":" + v, end=',')
    print('')


def set_gen_method():  # set集合推导式，可以从范围，字典，列表等等来生成set
    s = {i ** 2 for i in range(6)}
    print(s)
    print('==============================================')
    d = {'coming': 200, 'selling': 300, 'profit': 100}
    s = {d[i] for i in d.keys()}
    print(s)  # {200, 100, 300}
    print('==============================================')
    li = [-1, 20, -2, 30, -3, 40, -4, 50, -5, 60]
    s = {i for i in li if i > 0}  # 从列表中取出所有正数
    print(s)  # {40, 50, 20, 60, 30} set是无序的


def get_tuple_method():  # 注意元组也有推导式，返回的是生成器对象，需要使用元组构造函数将其变为元组
    d = {'coming': 200, 'selling': 300, 'profit': 100}
    t = (d[i] for i in d.keys())  # 返回的是生成器对象，需要使用元组构造函数将其变为元组,元组是有序，而且是不可变的
    t = tuple(t)
    print(t)
    t2 = (i**3 for i in range(6))
    t2 = tuple(t2)
    print(t2)


if __name__ == '__main__':
    # demo1()
    # set_demo()
    # set_travel()
    # set_gen_method()
    get_tuple_method()

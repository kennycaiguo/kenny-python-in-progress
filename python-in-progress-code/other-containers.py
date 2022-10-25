from collections import Iterable, Iterator, ChainMap, Counter, deque, defaultdict, namedtuple, OrderedDict
import csv

'''
 python的其他容器包括ChainMap, Counter, deque, defaultdict, namedtuple, OrderedDict等等
 其中比较重要的是Counter, deque, OrderedDict, namedtuple
'''


def deque_demo():  # 这是一个双向队列，可以在两端的任意一端添加删除元素
    dq = deque(['sxt', 'very', 'good'])
    # 添加元素
    dq.append('girls')  # 在右边添加
    dq.appendleft('friends')  # 在左边添加
    print(dq)
    dq.remove('friends')  # 移除
    print(dq)
    dq.popleft()  # 在左边弹出
    print(dq)
    dq.insert(1, "money")  # 在任意位置插入
    print(dq)
    dq.reverse()  # 反转，在原地操作，没有返回值
    print(dq)
    print(len(dq))
    li = ['i', 'love', 'u']
    # dq.extend(li)  # 将一个列表的元素添加到尾部
    # print(dq)  # deque(['girls', 'good', 'money', 'very', 'i', 'love', 'u'])
    dq.extendleft(li)  # 将一个列表的元素添加到头部,
    print(dq)  # deque(['u', 'love', 'i', 'girls', 'good', 'money', 'very'])


def named_tuple_demo():
    # 1.创建namedtuple类型
    Point = namedtuple('Point', ['x', 'y'])  # 创建namedtuple的方法namedtuple(元组名称, ’第一个成员名称, 第二个成员名称‘)，
    # 2.实例化一个namedtuple对象
    pt = Point(10, 20)
    print(pt)
    pt = Point(40, 50)
    print(pt)

    # 特殊方法_make
    a = [100, 20]
    pt = Point._make(a)
    print(pt)
    # 特殊方法_asdict(),返回一个OrderedDict
    print(pt._asdict())  # OrderedDict([('x', 100), ('y', 20)])
    # _replace() 方法 返回一个新的namedtuple对象实例
    new_pt = pt._replace(y=55)
    print(new_pt)
    # 特殊属性_fields
    Colors = namedtuple('Colors', 'red,green,blue')
    Pixels = namedtuple('Pixel', Point._fields + Colors._fields)  # 意思是这个命名元组有Point元组和Colors元组的所有字段，一共是5个
    pixels = Pixels(22, 33, 125, 255, 0)
    print(pixels)
    # 可以使用getattr()方法来获取属性值
    # print(getattr(pixels, 'x'))
    # for i in pixels:
    #        print(i)

    # 可以将一个字典解包传递给namedtuple类
    data = {'x': 50, 'y': 60}
    p = Point(**data)
    print(p)  # Point(x=50, y=60)
    # 文档字符串可以自定义，通过直接赋值给 __doc__ 属性:
    Book = namedtuple('Book', 'id,title,author')
    Book.__doc__ += ': Hardcover book in active collection'
    Book.id.__doc__ = '13-digit ISBN'
    Book.title.__doc__ = 'Title of first printing'
    Book.author.__doc__ = 'List of authors sorted by last name'
    b = Book("isbn-123456-xx", "how to meet a girl", "kenny")
    print(b.id)


def named_tuple_demo2():  #
    # 将namedtuple对象和文件数据关联起来
    Emp_record = namedtuple('Emp_record', 'name, age,sex, title, department, paygrade,salary')
    emp_map = map(Emp_record._make, csv.reader(open('emp.csv', 'r')))
    # print(list(emp_map))
    for emp in emp_map:
        # print(emp.name,emp.sex,emp.title,emp.salary)
        print(emp)
    Account = namedtuple('Account', 'owner balance transaction_count')
    default_acc = Account('<owner name>', 10000, 0)
    john_acc = default_acc._replace(owner='John stuward')
    john_acc = default_acc._replace(transaction_count=3)
    print(john_acc)


"""
  namedtuple子类化
"""


class Point(namedtuple('Point', 'x,y')):
    __slots__ = ()  # 子类设置 __slots__ 为一个空元组。通过阻止创建实例字典保持了较低的内存开销。

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point[x=%6.2f  y=%6.2f  hypot=%6.2f]' % (self.x, self.y, self.hypot)


def Counter_demo():
    """
    Counter 对象
     一个计数器工具提供快速和方便的计数
     Counter对象有一个字典接口，如果引用的键没有任何记录，就返回一个0
     Counter 对象的常用案例
    sum(c.values())                 # total of all counts
    c.clear()                       # reset all counts
    list(c)                         # list unique elements
    set(c)                          # convert to a set
    dict(c)                         # convert to a regular dictionary
    c.items()                       # convert to a list of (elem, cnt) pairs
    Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
    c.most_common()[:-n-1:-1]       # n least common elements
    +c                              # remove zero and negative counts

    """
    # 可以不传递参数
    cnt = Counter()
    # 传递列表
    cnt2 = Counter(['i', 'love', 'pussy', 'and', 'i', 'love', 'money', 'and', 'i', 'love', 'nice food'])
    print(cnt2)
    print(cnt2.most_common(3))  # 显示出现次数最多的项
    cnt3 = Counter([1, 2, 3, 4, 1, 3, 2, 4, 5, 6, 7, 8, 8, 9, 7, 7, 7, 7])  # Counter对象的key是列表的元素，value是它重复的次数
    # print(cnt3)
    print(cnt3.elements())
    # 传递字典
    ctr = Counter({'name': 3, 'sex': 2, 'age': 40})
    print(ctr)
    # 传递key=value
    ctr2 = Counter(cat=10, dog=5, duck=3)
    print(ctr2.elements())  # elements()方法返回包含counter对象的元素的一个对象，需要调用sorted方法才可以显示元素
    print(sorted(ctr2.elements()))  # elements()方法返回counter对象的元素
    # 量结构一样的Couner可以相减，是对应key的value相减,使用Counter对象1.subtract(Counter对象2)
    c = Counter(key1=100, key2=200, key3=300)
    d = Counter(key1=120, key2=250, key3=200)
    c.subtract(d)  # 注意subtract方法会修改原来的counter对象的值，它不返回值
    print(c)
    new_c = c.__add__(d)  # 这是加法返回一个新对象
    print(new_c)


def OrderedDict_demo():
    d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    # 创建OrderedDict时可以指定按key排序还是按value排序,也可以不排序，默认排序是从小到大
    # 按key排序
    print("=====================-====sorted by key===========================")
    od = OrderedDict(sorted(d.items(), key=lambda t: t[0]))  # t 表示每一个键值对，t[0]表示key,t[1]表示value
    print(od)
    print("=====================-====sorted by value===========================")
    # 按value排序
    od2 = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    print(od2)
    # 按key的长度排序,如果key的长度一样就按照首字母的ascii码来排序
    od3 = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
    print(od3)
    # for i in od3:  # 在这里i是key
    #     print(i, od3[i])  # 0k
    for k, v in od3.items():  # items()方法获取字典的每一个键值对
        print(k, v)  # ok


if __name__ == '__main__':
    # deque_demo()
    # named_tuple_demo()
    # named_tuple_demo2()
    Counter_demo()
    # OrderedDict_demo()
    # for p in Point(10,20),Point(100,200):
    #     print(p)

"""
操作类属性有三种方法：
1.使用@property装饰器操作类属性。
2.使用类或实例直接操作类属性（例如：obj.name，obj.age=18，del obj.age）
3.使用python内置函数操作属性。
属性存在的意义：
1、访问属性时可以制造出和访问字段完全相同的假象，属性由方法衍生而来，如果Python中没有属性，方法完全可以代替其功能。
2、定义属性可以动态获取某个属性值，属性值由属性对应的方式实现，应用更灵活。
3、可以制定自己的属性规则，用于防止他人随意修改属性值。
下面详细介绍三种操作类属性的方法：

1.使用@property装饰器操作类属性。
     定义时，在普通方法的基础上添加@property装饰器；属性仅有一个self参数，调用时无需括号；
   优点：
    1) @property装饰器可以实现其他语言所拥有的getter，setter和deleter的功能（例如实现获取，设置，删除隐藏的属性）
    2) 通过@property装饰器可以对属性的取值和赋值加以控制,提高代码的稳定性。
2.使用类或实例直接操作类属性

 缺点：对类的属性没有操作控制规则，容易被人修改。

3.使用python内置函数操作属性。
   1）getattr(obj, name[, default])：访问对象的属性，如果存在返回对象属性的值，否则抛出AttributeError异常。
   2）hasattr(obj,name)：检查是否存在某个属性，存在返回True，否则返回False。
   3）setattr(obj,name,value)：设置一个属性。如果属性不存在，会创建一个新属性，该函数无返回值。若存在则更新这个值。
   4）delattr(obj, name)：删除属性，如果属性不存在则抛出AttributeError异常，该函数也无返回值。
"""


# 1.使用@property装饰器操作类属性。
# 注意1，在需要变成顺序的getter方法上面添加@property装饰器
#    2. getter，setter，deleter的名字必须一样，在setter方法上面添加 @属性名.setter, deleter方法上面添加@属性名.deleter装饰器

class Goods(object):
    def __init__(self, name, value=50):
        self.name = name
        self.value = value

    @property
    def price(self):
        return self.value

    @price.setter
    def price(self, value):
        while value <= 0:
            value = int(input("价格必须大于0，请您重新输入:"))
        self.value = value

    @price.deleter
    def price(self):
        del self.value
        print("price has been deleted....")


def test_method1():
    apple = Goods('apple')
    apple.price = -1
    print(apple.price)
    del apple.price


# 2.使用类或实例直接操作类属性
class Employee(object):
    # 类属性
    Emps = 0

    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        Employee.Emps += 1  # 每创建一个员工，员工集合就增加1

    def total_emps(self):
        return Employee.Emps

    def __str__(self):
        return 'Employee[name:{e.name},age:{e.age},gender:{e.gender},salary:{e.salary}]'.format(e=self)


def test_method2():
    e = Employee('jacky', 18, 'male', salary=1000)
    print(e)
    print(e.total_emps())
    e = Employee('becky', 18, 'male', salary=1000)
    print(e)
    print(e.total_emps())


# 3.使用python内置函数操作属性。
class Person(object):

    @classmethod
    def set_name(cls, name):
        setattr(cls, "name", name)

    @classmethod
    def set_age(cls, age):
        setattr(cls, "age", age)

    @classmethod
    def set_sex(cls, sex):
        setattr(cls, "sex", sex)

    @classmethod
    def get_name(cls):
        return getattr(cls, "name")

    @classmethod
    def get_age(cls):
        return getattr(cls, "age")

    @classmethod
    def get_sex(cls):
        return getattr(cls, "sex")


def test_method3():
    p = Person()
    p.set_name("Jessieca")
    p.set_age(30)
    p.set_sex('female')
    print(p.get_name(), p.get_sex(), p.get_age())
    print(hasattr(p, 'name'))  # 查看对象是否有某个属性
    print(hasattr(p, 'age'))
    print(hasattr(p, 'tel'))
    # 在外面动态设置属性
    if not hasattr(p, 'tel'):
        setattr(p, 'tel', '13522288997')
    print(getattr(p, 'tel'))


# 4.私有property函数将几个方法绑定到一个属性在
class Game(object):
    def __init__(self):
        self.__name = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def del_name(self):
        del self.__name

    def __del__(self):
        print("对象被释放了。。。。")

    game = property(get_name, set_name, del_name, doc="游戏操作")  # 注意这里的顺序不能搞错，先getter，再setter，再deleter，然后是doc


def test_game():
    g = Game()
    g.game = "皇者荣耀"
    print(g.game)
    # del g.game


if __name__ == '__main__':
    # test_method1()
    # test_method2()
    # test_method3()
    test_game()

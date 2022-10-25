"""
python在类变量和实例变量
1.类变量属于类，它在类的所有方法外面定义的，是所有类是实例共享的。它可以通过类名.和类实例.来获取值，但是只能够通过类名来修改值
2.实例变量是在__init__(self,arg)方法中定义的变量，他属于类实例
需要注意的是类本身有一个__dict__属性，以字典的形式记录类的属性，类对象也有一个__dict__属性，它和类的__dict__属性是不同的
通过它无法找到类的属性！！！
如果为类对象添加一个和类属性同名的属性，而且属性值也相同，实际上不会创建新属性，它还是会引用类属性，这个一定要注意，只有当两个同名的属性值不一样，才会
创建新属性！！！（字符串属性除外）其实，空间是开辟了，只是它还是引用类属性，当我们修改了类同名属性的值，类实例才使用新开辟的空间
类其实可以调用实例方法的不过非常麻烦而且写法很别扭。
格式：类名.实例方法名称(类名(参数)) --->原理，通过类名(参数)的方法构造一个对象来替代self参数
"""


class ProgrammingLanguage(object):
    general_name = "计算机编程语言"  # 类属性，类对象可以读取属性不能修改属性
    rating = 10

    @classmethod  # 类方法，注意类实例也是可以调用类方法的
    def g_info(cls, general_name):
        print("This is a {}".format(general_name))

    @staticmethod
    def getRating(rating):
        return rating

    def __init__(self, name=None):  # 其实在__init__()方法之前，还有一个__new__(cls)方法，该方法在__init__()方法之前执行并且每创建一个对象执行一次
        self.name = name  # 对象属性  # __new__(cls)方法和__init__(self)方法的参数除了第一个以外，其余的必须要一致，否则抛异常

    def info(self):
        print("this is the {} programming language".format(self.name))


if __name__ == '__main__':
    c = ProgrammingLanguage(name='C ')
    print("used by class Name:", ProgrammingLanguage.general_name)  # used by class Name: 计算机编程语言
    print("used by instance", c.general_name)  # used by instance 计算机编程语言
    # c.general_name = "Computer Programming Language"
    # print(ProgrammingLanguage.general_name)  # 计算机编程语言,可见，通过类实例无法修改类属性，它只不过是为类实例添加一个同名的实例属性
    # print(c.general_name)  # Computer Programming Language 如果类实例的属性和类属性同名，使用类实例调用到的是类实例的属性
    # print(ProgrammingLanguage.name)  # 错误，不能通过类名来调用实例属性或者方法！！！

    c.general_name = "计算机编程语言"
    c.rating = 10
    # print(id(ProgrammingLanguage.general_name))
    print(id(c.general_name))
    # print(id(ProgrammingLanguage.rating))
    print(id(c.rating))
    ProgrammingLanguage.rating = 30
    print(c.rating)  # 还是10，此时因为类的同名属性的值修改了，实例对象就使用自己的同名属性
    print("=============================")
    c.info()
    # 用类名调用实例方法,不推荐使用
    ProgrammingLanguage.info(ProgrammingLanguage("Python "))  # this is the Python  programming language

    # 类方法
    ProgrammingLanguage.g_info(ProgrammingLanguage.general_name)

    # 调用静态方法
    print(ProgrammingLanguage.getRating(ProgrammingLanguage.rating))

    c.g_info(c.name)  # 类实例可以调用类方法

    print(c.getRating(c.rating))  # 类实例也是可以调用静态方法的

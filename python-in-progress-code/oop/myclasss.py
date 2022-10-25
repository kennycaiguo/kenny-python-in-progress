class Color(object):
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Square(object):
    def __init__(self, x):
        self.__side = x

    def get_side_len(self):
        return self.__side

    def set_side_len(self, x):
        self.__side = x

    def get_area(self):
        return self.__side ** 2


class ColorSquare(Color, Square):  # 括号类写多个类即为多重继承
    """
    # python多重继承中子类的初始化方法：
    按顺序一次调用每一个父类的构造方法，注意此时self是不能够省略的，否则报错
    """

    def __init__(self, color, x):
        Square.__init__(self, x)
        Color.__init__(self, color)
    # 除了__init__方法，上面方法都可以不写，因为它继承了父类的所有方法，当然这里可以写子类特有方法


def test_multi_inherit():  # 测试多重继承
    cs = ColorSquare(color='red', x=10)
    print("Color:", cs.get_color())
    print("side length:", cs.get_side_len())
    print("Area:", cs.get_area())


# 注意：python中以双下划线开头的变量是私有变量，但是由于python的动态语言特性，给人的错觉好像可以在外部修改私有变量，这是错误的
def test_private_var():
    c = Color('green')  # green
    print(c.get_color())
    # 尝试在外面修改__color属性
    c.__color = 'blue'
    print(c.get_color())  # 还是green，外部绑定的__color与self.__color不是同一个属性
    print(c.__color)  # blue,因为这个是外部添加的属性，不是类内部的私有属性


if __name__ == '__main__':
    # c = Color('red')
    # print(c.get_color())
    # test_multi_inherit()
    test_private_var()

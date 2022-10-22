from myclasss import Color, ColorSquare

'''
在python中，可以将在同一个目录下面的另外一个文件作为模块导入
也可以只导入指定的类或者方法
'''


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
    test_multi_inherit()
    # test_private_var()

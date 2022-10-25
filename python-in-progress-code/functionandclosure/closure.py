"""
python中闭包从表现形式上看，如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure)。
2.使用闭包注意的地方
2.1闭包无法修改外部函数的局部变量
2.2闭包无法直接访问外部函数的局部变量
  解决的方法：
　　1.在python3之前没有直接的解决方法，只能间接地通过容器类型来解决，因为容器类型不是存放在栈空间的，inner函数可以访问到。

def outer():
    x = [5]
    def inner():
        x[0] *= x[0]
        return x[0]
    return inner

print(outer()())  #25
原文链接：https://blog.csdn.net/Yeoman92/article/details/67636060
   2.python3通过nonlocal关键字来解决，该语句显式的指定a不是闭包的局部变量。

def outer():
    x = 5
    def inner():
        nonlocal x #把x声明为非局部变量
        x *= x
        return x
    return inner

print(outer()())
原文链接：https://blog.csdn.net/Yeoman92/article/details/67636060

闭包的作用
　　说了这么多，不免有人要问，那这个闭包在实际的开发中有什么用呢？闭包主要是在函数式开发过程中使用。以下介绍两种闭包主要的用途。

用途1：当闭包执行完后，仍然能够保持住当前的运行环境。
　　比如说，如果你希望函数的每次执行结果，都是基于这个函数上次的运行结果。我以一个类似棋盘游戏的例子来说明。假设棋盘大小为50*50，左上角为坐标系原点(0,0)，
我需要一个函数，接收2个参数，分别为方向(direction)，步长(step)，该函数控制棋子的运动。棋子运动的新的坐标除了依赖于方向和步长以外，
当然还要根据原来所处的坐标点，用闭包就可以保持住这个棋子原来所处的坐标。

origin = [0, 0]
legal_x = [0, 50]
legal_y = [0, 50]
def create(pos=origin):
    def player(direction,step):
        # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等
        # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。
        new_x = pos[0] + direction[0]*step
        new_y = pos[1] + direction[1]*step
        pos[0] = new_x
        pos[1] = new_y
        #注意！此处不能写成 pos = [new_x, new_y]，因为参数变量不能被修改，而pos[]是容器类的解决方法
        return pos
    return player

player = create() # 创建棋子player，起点为原点
print player([1,0],10) # 向x轴正方向移动10步
print player([0,1],20) # 向y轴正方向移动20步
print player([-1,0],10) # 向x轴负方向移动10步


输出为：

 [10, 0]
 [10, 20]
 [0, 20]

用途2：闭包可以根据外部作用域的局部变量来得到不同的结果
　　这有点像一种类似配置功能的作用，我们可以修改外部的变量，闭包根据这个变量展现出不同的功能。比如有时我们需要对某些文件的特殊行进行分析，先要提取出这些特殊行。

def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter

　　如果我们需要取得文件”result.txt”中含有”pass”关键字的行，则可以这样使用例子程序

filter = make_filter("pass") filter_result = filter("result.txt")

　　以上两种使用场景，用面向对象也是可以很简单的实现的，但是在用Python进行函数式编程时，闭包对数据的持久化以及按配置产生不同的功能，是很有帮助的。

原文链接：https://blog.csdn.net/Yeoman92/article/details/67636060
"""


def outer(x):
    def inner(y):  # inner引用了outer的参数，inner就是闭包
        return x * y

    return inner


def out_fun():
    x = 10
    print('x=', x)

    def in_fun():
        x = 100
        print('x=', x)

    in_fun()

    print('x=', x)


def Outter():
    # x = 5
    x = [5]  # 这样子也是可以访问的

    def Inner():
        # nonlocal x   # 闭包无法直接使用外部函数的局部变量，如果非得使用，需要在声明一个同名的nonlocal变量
        x[0] = x[0] + 5
        return x

    return Inner


def f1():
    n = 999

    def f2():
        print(n)  # 其实闭包是可以读取外函数的变量但是不能修改或者用来运算

    return f2


def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name, content)

    return add_tag


def test_tag():
    content = "div"
    _tag = tag('div')
    print(_tag(content))  # <div>div</div>
    print("===================")
    print(tag('strong')("hello"))


'''
将列表转为字符串
'''


def list_to_string(*args):
    def inner():
        lst = list(map(str, *args))  # 这里需要解包
        str_lst = "-".join(lst)
        print(str_lst)

    return inner


# 2层闭包：是一个3层函数，只要闭包存在，闭包外函数的资源不会被回收，即使外函数执行完毕，因为此时还有闭包在引用他们
def f(a):
    def g(b):
        def k(c):
            return a + b + c

        return k

    return g


if __name__ == '__main__':
    # inner = outer(100)
    # print(inner(10))
    # print(outer(10)(20))  # 还可以这么用
    # out_fun()
    # print(Outter()())
    # res = f1()
    # res()
    # test_tag()
    # list_to_string([1,3,4])()
    # f1=f(1)
    # f2=f1(2)
    # num = f2(3)
    # print(num)  # 6
    print(f(1)(2)(3))  # 6 另外一种写法

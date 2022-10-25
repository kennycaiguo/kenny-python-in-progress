"""
Python崇尚“鸭子类型”

对于鸭子模型常见的说法是：“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”

鸭子类型（英语：duck typing）在程序设计中是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，
而是由“当前方法和属性的集合”决定

在鸭子类型中，关注点在于对象的行为能做什么；而不是关注对象所属的类型。例如，在不使用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为"鸭子"的对象，
并调用它的"走"和"叫"方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的"走"和"叫"方法。如果这些需要被调用的方法不存在，
那么将引发一个运行时错误。任何拥有这样的正确的"走"和"叫"方法的对象都可被函数接受的这种行为引出了以上表述，这种决定类型的方式因此得名

鸭子类型通常得益于"不"测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用

在常规类型中，我们能否在一个特定场景中使用某个对象取决于这个对象的类型，而在鸭子类型中，则取决于这个对象是否具有某种属性或者方法——即只要具备特定的属性或方法，
能通过鸭子测试，就可以使用。
2、“鸭子类型”从何而来
2.1 多态
先来看看“多态”

大学时学习过C、Java基础这一类强类型语言，面向对象编程的三大特性之一有个概念叫做“多态”

简单来说，定义时的类型和运行时的类型不一样就是多态

更通俗的来说，多态是指一类事物有多种形态。比如动物有多种形态，人、狗、猫等等

放到二进制的世界，例如文件，文件有多种形态：文本文件、可执行文件

总而言之，多态即某类的再分类，再分的每一类就是父类的多种形态的一种
2.3 鸭子类型产生
在上面的例子中order.account(pay_obj)中pay_obj不需要类型声明，而java在使用时要定义好类型

（order.account(Payment pay_obj)），所以你传入别的类型对象一定报错

但是python因为是动态语言所以传入的对象只要拥有调用的方法即可视为Payment类型对象，这就是所谓的鸭子类型

class Duck():
    def walk(self):
        print('I walk like a duck')
    def swim(self):
        print('i swim like a duck')

class Person():
    def walk(self):
    　　print('this one walk like a duck')
    def swim(self):
    　　print('this man swim like a duck')
可以很明显的看出，Person类拥有跟Duck类一样的方法，当有一个函数调用Duck类，并利用到了两个方法walk()和swim()。我们传入Person类也一样可以运行，
函数并不会检查对象的类型是不是Duck，只要他拥有walk()和swim()方法，就可以正确的被调用
"""
from abc import ABCMeta, abstractmethod  # (抽象方法)


class Payment(metaclass=ABCMeta):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @abstractmethod  # @abstractmethod表示下面一行中的pay方法是一个必须在子类中实现的方法
    def pay(self, *args, **kwargs):
        pass


class AliPay(Payment):
    def pay(self):
        # 支付宝提供了一个网络上的联系渠道
        print('%s通过支付宝消费了%s元' % (self.name, self.money))


class WeChatPay(Payment):

    def pay(self):
        # 微信提供了一个网络上的联系渠道
        print('%s通过微信消费了%s元' % (self.name, self.money))


class Order(object):

    def account(self, pay_obj):
        pay_obj.pay()


if __name__ == '__main__':
    ali_pay = AliPay('alipay',1000)
    wc_pay = WeChatPay('wechat pay',2000)
    order = Order()
    order.account(ali_pay)
    order.account(wc_pay)

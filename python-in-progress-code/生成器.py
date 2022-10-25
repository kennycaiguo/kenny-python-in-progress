"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。
请务必注意：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。他们是不同的对象
"""


# 我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
def generaor_demo1():
    t = (x * x for x in range(10))
    for i in t:
        print(i, end=',')
    print()


# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


def get_generator_ret_val():
    gen = fibonacci(6)
    while True:
        try:
            x = next(gen)
            print(x)
        except StopIteration as e:
            print("return value:", e.value)
            break

def test_gen():
    f = fibonacci(5)
    for i in f:
        print(i, end=',')
    print()


if __name__ == '__main__':
    # generaor_demo1()
    # test_gen()
    get_generator_ret_val()

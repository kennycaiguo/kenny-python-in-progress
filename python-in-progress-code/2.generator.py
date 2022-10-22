# 生成器
# 生成器最佳应用场景是： 你不想同一时间将所有计算出来的大量
# 结果集分配到内存当中， 特别是结果集里还包含循环
def generator():
    for i in range(10):
        yield i

# 利用生成器产生斐波那契数列
def febonacci(n):
    a = b = 1
    for x in range(n):
        yield a
        a,b = b,a+b

#  注意，str是一个可迭代对象，但是它不是一个迭代器，迭代方法是先运行iter方法，产生一个迭代器，再使用next方法来操作这个迭代器
def iter_str(my_str):
    str_iter = iter(my_str)
    while True:
        print(next(str_iter))


if __name__ == '__main__':
    # for i in generator():
    #     print("$", i)
    # for x in febonacci(100):
    #     print(x,"\n")
    iter_str("hello,pussy")

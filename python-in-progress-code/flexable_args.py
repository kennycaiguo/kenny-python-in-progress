"""
python中的可变参数
*arg 表示的是一个可变长度元组，实际上可以长度列表元组和set但是需要解包
**kw 表示接收类似于关键参数一样赋值的形式的多个实参放入字典中（即把该函数的参数转换为字典）。
"""


def printargs(*args):
    for a in args:
        print(a, end=",")
    print()


if __name__ == '__main__':
    printargs(1,2,"hello girls",True)

from io import StringIO

"""
StringIO的引入：
内存中的IO
首先必须要搞清一个问题，就是为什么要有内存级别的IO？

之前说的磁盘上的文件，就是将数据持久化到磁盘的一块区域，供后面重复使用。其优点就是持久化稳定不丢失，但是缺点也很明显，就是每次要使用都要从磁盘读入，相对内存而言很缓慢。

如果只是短时间的重复利用，并不希望长期持久化，而且对速度的要求比较高，这时候就可以考虑缓存。说到缓存，很多朋友就想到redis，熟悉python的朋友还会想到装饰器和闭包函数。

不过python已经原生为我们准备好了类文件对象（file-like object），这种对象在内存中创建，可以像文件一样被操作。
StringIO和ByteIO就是这样的对象
"""


def StringIO_demo1():
    with StringIO() as f:
        c = f.write("hello ,sexy girls")
        print('写入的字节数：%d' % c)  # 写入的字节数：17
        # 注意：执行了write方法后文件指针移动到17，在读取是读不到数据的，必须将指针移动回来
        # f.seek(0)  # 移动到开始位置
        # print(f.read())  # hello ,sexy girls
        # 但是获取全部值方法不受这个标志位影响
        print(f.getvalue())  # hello ,sexy girls


def StringIO_demo2():
    content = '''
    StringIO is a type of menIO
    it works just like a file
    it can write data to memory
    and it can also read data from it 
    '''
    with StringIO() as f:
        c = f.write(content)
        # 读取之前需要把指针移动到开始
        f.seek(0)
        str_read = f.readline()
        while str_read:
            print(str_read)
            str_read = f.readline()
        print("done!!!")


def StringIO_to_file():
    content = '''StringIO is a type of menIO
     it works just like a file
     it can write data to memory
     and it can also read data from it 
     '''
    with StringIO() as f, open('stringio.txt', 'w', encoding='utf-8') as dst:
        c = f.write(content)
        # 读取之前需要把指针移动到开始
        f.seek(0)
        str_read = f.readline()
        while str_read:
            dst.write(str_read.strip() + '\n')
            str_read = f.readline()
        print("done!!!")


def file_to_StringIO(filename):
    with open(filename, 'r', encoding='utf-8') as f, StringIO() as s:
        data_read = f.readline()
        while data_read:
            s.write(data_read.strip() + '\n')
            data_read = f.readline()
        print(s.getvalue())


if __name__ == '__main__':
    # StringIO_demo1()
    # StringIO_demo2()
    # StringIO_to_file()
    file_to_StringIO('stringio.txt')

def read_demo1():
    f = open("test.txt", 'r', encoding='utf-8')
    content = f.read()  # read() 方法没有参数可以一次读取所有内容，返回的是一个字符串，也可以添加参数表示一次读取多少个字符
    print(type(content))
    f.close()


def read_demo2():  # 一行一行读取
    f = open("test.txt", 'r', encoding='utf-8')
    line = f.readline()
    while line:
        print(line, end=' ')
        line = f.readline()
    f.close()


def read_demo2():  # 一次读取所有行返回列表
    f = open("test.txt", 'r', encoding='utf-8')
    lines = f.readlines()
    print(lines) # ['人生苦短，好好爱你的女人，多多...\n', '人生苦短，好好爱你的女人，多多...\n', '人生苦短，好好爱你的女人，多多...\n']


if __name__ == '__main__':
    # read_demo1()
    read_demo2()

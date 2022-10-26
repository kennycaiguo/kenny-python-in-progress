def copyfile(src, dst):  # 循环读取一行写一行
    s = open(src, 'r', encoding='utf-8')
    d = open(dst, 'w', encoding='utf-8')
    line = s.readline()
    while line:
        d.write(line)
        line = s.readline()
    d.close()
    s.close()
    print("done!!!")


def copyfile2(src, dst):  # 一次读入全部和一次写入全部,这种方法不好，当文件太大就有可能很卡
    s = open(src, 'r', encoding='utf-8')
    d = open(dst, 'w', encoding='utf-8')
    content_str = s.read()
    d.write(content_str)
    d.close()
    s.close()
    print("done!!!")


def copyfile_b(src, dst):  # 循环读取一行写一行,readline如果是'rb' 方式读取返回byte，如果是'r'方式读取返回字符串
    s = open(src, 'rb')  # 二进制的方法还可以拷贝图片
    d = open(dst, 'wb')
    line = s.readline()
    while line:
        d.write(line)
        line = s.readline()
    d.close()
    s.close()
    print("done!!!")


# 使用with操作文件的好处是它可以帮你关闭流
def copyfile_b_with(src, dst):  # 循环读取一行写一行,readline如果是'rb' 方式读取返回byte，如果是'r'方式读取返回字符串
    with open(src, 'rb') as s, open(dst, 'wb') as d:  # 二进制的方法还可以拷贝图片
        line = s.readline()
        while line:
            d.write(line)
            line = s.readline()
        d.close()
        s.close()
        print("done!!!")


if __name__ == '__main__':
    # copyfile("test.txt", "testcopy.txt")  # ok
    # copyfile2("test.txt","textcopy2.txt")
    # copyfile_b("test.txt", "testcopyb.txt")
    # copyfile_b("hy3.jpg", "g.jpg")
    # copyfile_b("cyd.docx", "c.docx")
    # copyfile_b("laugh.mp4", "l.mp4")
    copyfile_b_with("laugh.mp4", "l.mp4")

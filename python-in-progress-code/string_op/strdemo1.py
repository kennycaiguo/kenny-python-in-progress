def build_str_demo():
    str2 = 'hell0' \
           'world of girls'  # 在python中，如果一个字符串太长，可以使用反斜杠'\'将其折成多行，但是在删除的时候会输出为一行
    print(str2)
    str3 = 'hello' 'sexy girls'  # 在python中，两个挨在一起的字符串会被连接成一个字符串
    print(str3)
    str4 = '''hello 
    world of sexy
    and very pretty girls'''  # 使用三引号包裹的字符串会保留定义时的书写格式
    print(str4)


def transfered_meaning():  # python 转义字符
    """
    表 1 Python 支持的转义字符
    转义字符	说明
    \n	换行符，将光标位置移到下一行开头。
    \r	回车符，将光标位置移到本行开头。
    \t	水平制表符，也即 Tab 键，一般相当于四个空格。
    \a	蜂鸣器响铃。注意不是喇叭发声，现在的计算机很多都不带蜂鸣器了，所以响铃不一定有效。
    \b	退格（Backspace），将光标位置移到前一列。
    \\	反斜线
    \'	单引号
    \"	双引号
    \	在字符串行尾的续行符，即一行未完，转到下一行继续写。

    """
    path = 'c:\now'
    print(path)  # c:
    # ow 分成两行输出因为'\n'是转义字符，表示换行符
    path = 'c:\\now'  # 解决办法1 使用'\\'代替'\'
    print(path)  # c:\now

    s = 'give me \ashtray'  # give me shtray  # \a表示蜂鸣器响铃
    print(s)
    s2 = 'get \taway from me!'
    print(s2)  # get 	away from me!  \t表示tab
    s3 = 'hello  !\b!\b!\b'  # hello  \b 表示退格键
    print(s3)


def no_transfer_meaning():  # 解决转义字符的问题
    # 1 用\\ 代替\
    s = 'the path is d:\new'
    print(s)  # 字符串被分成两行而且'\n'不见了
    s2 = 'the path is d:\\new'  # the path is d:\new
    print(s2)
    # 2 在字符串前面加r,这个方法比较好,注意有时候用了r还会报错需要将最后一个'\'换成'\\'
    s3 = r'the path is d:\new'  # the path is d:\new
    print(s3)
    s4 = r'path: "f:\funny\"'  # 如果直接 r'path: f:\funny\'这么写直接报错需要将最后一个'\'换成'\\'，\'是转义字符或者也可以yong双引号就其包裹
    print(s4)


def format_demo():  # 一些比较有用的字符串格式化
    s1 = '{}:{},{}:{}'.format('name', 'Jack', 'age', 18)
    print(s1)
    s2 = '{name} is {age} years old he is the boss,he has{num} workers '.format(age=40, num=300, name='Kenny')
    print(s2)
    s3 = '{0},{1}，{0}!!!'.format('lenny', 'go')  # 可以使用索引而且索引能够重复使用
    print(s3)
    s4 = 'i would like {:$<8} dallors'.format(10000)  # '<'表示左对齐，如果位数不够在右边补齐
    print(s4)
    s5 = 'This would cost {:$^8} dollars'.format(100)  # '^'表示需要替换的值居中，左右两边补齐，如果不能平分，多余的往右边补
    print(s5)
    s6 = 'The beef is very dear!,it cost c{:$>8} per kilo!!！'.format(9000)  # '<'表示右对齐，如果位数不够在左边补齐
    print(s6)
    print('{:,}'.format(123123))  # 123,123,这里的','表示千分位
    print('{:.2f}'.format(123.45678))  # 123.46,这里的'.2f'表示保留2位小数
    # 上面这两个可以组合使用
    print('{:,.2f}'.format(123123.234567))  # 123,123.23 ',.2f'
    # d表示十进制，x表示十六进制，o表示八进制，b表示二进制
    print('int:{0:d};hex:{0:x};oct:{0:o};bin:{0:b}'.format(47))  # int:47;hex:2f;oct:57;bin:101111
    # 访问列表元素
    print('{0[0]},{0[1]}'.format(['hello','world']))  # hello,world
    print('{0[0][0]},{0[1][0]}'.format(['hello','world']))  # h,w
    print('{0[0]},{0[1]}'.format([1000,2000]))  # 1000,2000

if __name__ == '__main__':
    # build_str_demo()
    # transfered_meaning()
    # no_transfer_meaning()
    format_demo()

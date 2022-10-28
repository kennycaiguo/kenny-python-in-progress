"""
python中的字符串API
1. 切片操作
2. split(): 将字符串以指定字符分割为列表
3. join(): 将列表以指定字符合并为字符串
4.replace(): 替换, 将旧字符串替换为新字符串
5. lstrip(): 将字符串左边的空白去除
6. rstrip(): 将字符串右边的空白去除
7. strip(): 去除字符串两端空白
8. 字符串每个单词首字母大写
"""


def str_api_demo():
    # 0. 切片

    name = "Geek"
    # 从右边第一个截取到右边第二个不包含第三个
    print("=====================")
    print(name[:-3:-1])  # ek

    # Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
    # 如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
    # 1.str.splitlines(num=string.count(‘\n’))
    str1 = 'ab c\n\nde fg\rkl\r\n'
    print(str1.splitlines())  # ['ab c', '', 'de fg', 'kl']

    str2 = 'ab c\n\nde fg\rkl\r\n'
    print(str2.splitlines(True))  # ['ab c\n', '\n', 'de fg\r', 'kl\r\n']

    # 2. split(分隔符,分割次数): 将字符串以指定字符分割为列表，默认全部分割完但可以设置分割次数如果是1，就只分割第一次
    _str = "hello word and geek and python"
    _strList = _str.split(" ")  # ["hello", "word", "and", "geek", "and", "python"]
    print(_strList)
    _strList = _str.split(" ",1)  # ['hello', 'word and geek and python']
    print(_strList)
    print("=====================")
    # 3. join(): 将列表以指定字符合并为字符串
    # 用空格将列表合并成字符串
    print(" ".join(_strList))  # "hello word and geek and python"
    print("---------------------------")
    # 4. replace(): 替换, 将旧字符串替换为新字符串
    _str = "hello word and geek and python"
    # replace会返回一个新字符串，不会修改原字符串，默认不填替换次数就是全部替换
    print(_str.replace("and", "&&", 1))  # "hello word && geek and python"
    print("=====================")
    # 5. lstrip(): 将字符串左边的空白去除
    _str = "    ladies and gentalmen ,please say hello to Jack "
    print(_str.lstrip())  # "hello word and geek and python "
    print("=====================")
    # 6. rstrip(): 将字符串右边的空白去除

    _str = " I guess i have falled in love with python       "
    print(_str.rstrip())  # " hello word and geek and python"
    print("=====================")
    # 7. strip(): 去除字符串两端空白如果括号有参数，则移除字符串两端指定的字符

    _str = "  #hello word and geek and python#   "
    print(_str.strip())  # "hello word and geek and python"
    _str = 'learn to walk before you learn to run'
    print(_str.strip('un'))  # learn to walk before you learn to r
    # 8. 字符串每个单词首字母大写

    _str = "hello word and geek and python"
    # 字符串每个单词首字母大写
    print(_str.title())  # "Hello Word And Geek And Python"


def str_api_demo2():
    # 首字母大写str.capitalize()
    _str = "let's study python together"
    print(_str.capitalize())  # Let's study python together

    # 原字符居中，空格填充至width长度,当width参数比字符串的长度大才有用str.center(width,[,fill]),还可以指定填充的字符
    _str = 'love me'
    _str = _str.center(20, '♥')
    print(_str)  # ♥♥♥♥♥♥love me♥♥♥♥♥♥♥

    # 获得字符串中某一个子串的数目,计算出现次数，可指定范围str.count(substring,beg=0,end=len(string))
    _str = "i love money,i love sex,i love girls,i love nice big house,i love cars"
    print(_str.count('love'))  # 5

    # 是否以某字符或者字符串结尾str.endswith(suffix,beg=0,end=len(string))
    _str = 'work hard play hard,have sex....so hard....'
    print(_str.endswith('hard'))  # False
    print(_str.endswith('....'))  # True
    print(_str.endswith('.'))  # True
    print('*********************************************')
    # str.startswidth(), 判断一个字符串是否是一一个字串开头
    print(_str.startswith('work'))  # True
    print(_str.startswith('w'))  # True
    print('***********************************************')
    # 把字符串中tab转为空格，默认8个,可以修改str.expandtabs(tabsize=8)
    _str = "hi,i love u   and i will do anything for you"
    print(_str.expandtabs(50))

    # 检测是否包含substr，存在返回开始索引，否则返回-1 str.find(substr,beg=0,end=len(str))
    _str = "hi,i love u   and i will do anything for you"
    print(_str.find('love'))  # 5
    # str.rfind(str,beg=0,end=len(string)) 同find，右边开始,找到的字串的索引还是从头开始计算的
    print(_str.rfind('love'))  # 5
    # index同find，不存在报异常,ValueError
    print(_str.index('love'))  # 5
    # str.rindex(str,beg=0,end=len(string)) 同index,右边开始
    print(_str.rindex('love'))  # 5
    # str.swapcase() 反转string中大小写. 字符串中小写转大写，大写转小写
    _str = 'This Is A Game'
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(_str.swapcase())  # tHIS iS a gAME
    # str.translate(),用replace不好吗？，应该不常用的？
    # use a dictionary with ascii codes to replace 83 (S) with 80 (P):
    mydict = {83:  80}
    txt = "Hello Sam!"
    print(txt.translate(mydict))  # Hello Pam!


def str_api_demo3():
    # str.join(seq) 以string作为分隔符，seq中所有元素合并为新的字符串. 将原字符串插入参数字符串中的每两个字符之间
    lst = ['This', 'girl', 'is', 'so', 'good', '!']
    print(" ".join(lst))  # This girl is so good !

    # str.ljust(width) 返回一个原字符串左对齐，右边空格补充至长度width，可以指定填充字符
    _str = 'bad girl'
    print(_str.ljust(20,'*'))  # bad girl************
    print('------------------------')
    # str.rjust(width) 右对齐，空格补齐
    print(_str.rjust(30, '♥'))  # ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥bad girl
    print('------------------------')
    # str.lower() 转小写. 将字符串全部转为小写
    print('This girl is so good !'.lower()) # this girl is so good !
    # string.upper() 转大写. 将字符串全部转为大写
    print('i love girls'.upper())  # I LOVE GIRLS
    # str.lstrip() 截掉左侧的空格
    print('     This girl is so good!'.lstrip())  # This girl is so good!
    # str.rstrip() 截掉右侧的空格
    print('This girl is so good!     '.rstrip())  # This girl is so good!

    # str.partition(substr) 返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。只分一次
    print('www.runoob.com'.partition('.'))  # ('www', '.', 'runoob.com')
    # str.rpartition(str) 同partition，右边开始
    print('www.runoob.com'.rpartition('.')) # ('www.runoob', '.', 'com')
    print('♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')


def str_isxx_demo():  # 字符串中的isxx函数
    # 至少一个字符，且所有字符均为字母或数字，True. 检测字符串是否只包含0-9A-Za-z str.isalnum()
    zfc = '12345'
    print(zfc.isalnum())  # True
    zfc = 'k12345'
    print(zfc.isalnum())  # False
    zfc = '12345_'
    print(zfc.isalnum())  # False '-'既不是字母也不是数字

    # str.isalpha() 至少一个字符，所有字符都是字母，True. 检测字符串是否只包含字母
    zfc = 'k12345'
    print(zfc.isalpha())  # False

    # str.isdecimal()只包含十进制数
    zfc = '12345'
    print("====================================")
    print(zfc.isdecimal())  # True
    zfc = 'k12345'
    print(zfc.isdecimal())  # False
    print("====================================")
    # str.isdigit()只检测字符串是否仅包含数字
    zfc = 'k12345'
    print(zfc.isdigit())  # False
    zfc = '12345'
    print(zfc.isdigit())  # True
    print('#############################################')
    # str.islower() 检测字符串是否全部为小写字母
    print('i love you'.islower())  # True
    print('I love you'.islower())  # False
    print('#############################################')
    # str.isnumeric() 只含数字字符,True
    print('1234567'.isnumeric())  # True
    print('123b4567'.isnumeric())  # False
    # str.isspace() 只包含空格，True. 检测字符串是否均为空白字符
    print('#############################################')
    print('     '.isspace())  # True
    print('  i   '.isspace())  # False
    print('-------------------------------------------------')
    # str.istitle() 检测字符串中的每一个单词是否为首字母大写
    print('This is a dog'.istitle())  # False
    print('This Is A Dog'.istitle())  # True
    print('#=' * 20)
    # str.isupper()检测字符串是否均为大写字母
    print('So Good'.isupper())  # False
    print('SO GOOD'.isupper())  # True


if __name__ == '__main__':
    str_api_demo()
    # str_api_demo2()
    # str_api_demo3()
    # str_isxx_demo()

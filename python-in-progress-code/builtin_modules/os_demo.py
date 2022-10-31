import os
from pathlib import Path
"""
os就是“operating system”的缩写，顾名思义，os模块提供的就是各种 Python 程序与操作系统进行交互的接口。通过使用os模块，一方面可以方便地与操作系统进行交互，
另一方面页可以极大增强代码的可移植性。如果该模块中相关功能出错，会抛出OSError异常或其子类异常。

 注意
 如果是读写文件的话，建议使用内置函数open()；
 如果是路径相关的操作，建议使用os的子模块os.path；
 如果要逐行读取多个文件，建议使用fileinput模块；
 要创建临时文件或路径，建议使用tempfile模块；
 要进行更高级的文件和路径操作则应当使用shutil模块。
 

当然，使用os模块可以写出操作系统无关的代码并不意味着os无法调用一些特定系统的扩展功能，但要切记一点：一旦这样做就会极大损害代码的可移植性。

此外，导入os模块时还要小心一点，千万不要为了图调用省事儿而将os模块解包导入，即不要使用from os import *来导入os模块；否则os.open()将会覆盖内置函数open()
，从而造成预料之外的错误
"""


def os_demo1():
    print(os.name)  # nt
    print(os.curdir)  # .
    print(os.environ['HOMEPATH'])  # 用户目录\Users\Administrator.WIN-A6BUMH274M6
    print(os.path.abspath(__file__)) # 当前文件的绝对路径 F:\Projects_f\pycharm-edu-projs\python基础进阶\python-in-progress-code\builtin_modules\os_demo.py
    # os.getenv()和os.putenv:分别用来读取和设置环境变量
    print(os.getenv("JAVA_HOME"))
    print('---------------------------------------')
    e = os.environ
    path_var = e.get('path')
    print(path_var)  # 获取path环境变量
    print('----------------------------------------')
    print(os.getcwd())  # 获取当前路径
    # os.stat（file）:获得文件属性
    print(os.stat('os_demo.py'))
    print(os.linesep)
    print(os.path.split(__file__)[1])  # 从文件的绝对路径中分离出文件名os_demo.py
    print(os.path.isfile(__file__))  # True
    print(os.path.exists(__file__))  # True
    print(os.path.getsize(__file__))  # 2577
    print(os.path.isabs(__file__))  # True
    print(os.path.splitext(os.path.split(__file__)[1]))  # ('os_demo', '.py')将文件的基本名和扩展名分开
    path = "d:\learn\python"
    file = 'learnpython.txt'
    print(os.path.join(path,file))  # d:\learn\python\learnpython.txt
    print(os.path.basename('d:\learn\python\learnpython.txt'))  # 返回文件名 learnpython.txt
    print(os.path.dirname(__file__))
    os.system('copy hello.txt hello1.txt')  # 调用系统的复制命令
    os.popen('copy hello.txt hello2.txt')


def os_walk_demo(path):
    for item in os.walk(path):
        print(item)


def get_path_files(file_dir):

    list_directory = os.listdir(file_dir)
    filelists = []
    print(list_directory)
    for directory in list_directory:
        # os.path 模块稍后会讲到
        if os.path.isfile(directory):
            filelists.append(directory)
    return filelists



if __name__ == '__main__':
    os_demo1()
    # os_walk_demo('.')
    # print(get_path_files('.\\a\\'))
    # print(get_path_files('.\\b\\'))

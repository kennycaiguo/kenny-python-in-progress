import multiprocessing, time, os

"""
python创建进程的2种方式：
1.直接使用multiprocessing.Process(target="",args=(,))创建
2.编写一个类继承multiprocessing.Process，重写run方法
"""


def tesk1(name):
    print("子进程%s正在运行" % name)
    print("子进程%s的id=%d" % (name, os.getpid()))


def process_demo1():
    print("父进程的id=%s" % os.getpid())
    p1 = multiprocessing.Process(target=tesk1, args=(1,))
    p2 = multiprocessing.Process(target=tesk1, args=(2,))
    print("子进程启动")
    p1.start()
    p2.start()
    time.sleep(5)
    print("父进程结束。。。")


class TaskProcess(multiprocessing.Process):
    # 带参数创建必须重写__init__方法
    def __init__(self, arg):
        super(TaskProcess, self).__init__()  # 调用父类的初始化函数
        self.arg = arg

    def run(self) -> None:
        print("子进程%s正在运行" % self.arg)
        print("子进程%s的id=%d" % (self.arg, os.getpid()))


def process_demo2():
    print("父进程的id=%s" % os.getpid())
    p1 = TaskProcess(1)
    p2 = TaskProcess(2)
    time.sleep(2)
    print("子进程启动")
    p1.start()
    p2.start()
    print(p1.is_alive())
    print(p2.is_alive())
    time.sleep(5)
    print("父进程结束。。。")


if __name__ == '__main__':
    # process_demo1()
    process_demo2()

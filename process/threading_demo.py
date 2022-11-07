"""
python中的进程相关编程,进程需要线程来运行
创建线程有两个方法1.直接使用threading.Thread()类来创建，
            方法2.创建一个类继承threading.Thread()类，需要自己实现run方法
"""
import threading
import time


def task1():
    for i in range(5):
        print("hello," + threading.current_thread().name, i)
        time.sleep(1)


def main1():
    # 创建子线程
    th = threading.Thread(target=task1, name="TaskThread")
    th.start()  # 启动子线程
    # 主线程任务
    for j in range(5):
        print("main:" + threading.main_thread().name, j)
        print(th.name + "is alive:", th.isAlive())
        time.sleep(2)


def main2():
    # 创建子线程
    th = threading.Thread(target=task1, name="TaskThread")
    th.start()  # 启动子线程
    th.join()  # 让子线程执行完成
    # 主线程任务
    for j in range(5):
        print("main:" + threading.main_thread().name, j)
        print(th.name + "is alive:", th.isAlive())
        time.sleep(2)


class TaskThread(threading.Thread):  # 创建线程类从threading.Thread派生
    def __init__(self, name=None):
        threading.Thread.__init__(self, name=name)

    def run(self) -> None:
        for i in range(5):
            print("running:" + threading.current_thread().name, i)
            time.sleep(1)


def main3():
    th = TaskThread("My Task Thread")
    th.start()
    # 主线程任务
    for j in range(5):
        print("main:" + threading.main_thread().name, j)
        print(th.name + "is alive:", th.isAlive())
        time.sleep(2)


def main4():
    th = TaskThread("My Task Thread1")
    th.start()
    th2 = TaskThread("My Task Thread2")
    th2.start()
    print(threading.activeCount())
    # 主线程任务
    for j in range(5):
        print("main:" + threading.main_thread().name, j)
        print(th.name + "is alive:", th.isAlive())
        print(threading.activeCount())
        time.sleep(2)


if __name__ == '__main__':
    # main1()
    # main2()
    # main3()
    main4()

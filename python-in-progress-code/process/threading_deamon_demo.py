"""
daemon线程是主线程的守护线程，它会随着主线程的结束而结束
python3默认创建的不是守护线程，可以通过setDaemon来设置，或者在创建线程的时候将daemon属性设置为True
"""
import threading
import time


def job1():
    print("begin job...")
    time.sleep(5)
    print('end job...')


def main1():
    t1 = threading.Thread(target=job1, daemon=False)
    t1.start()
    t2 = threading.Thread(target=job1, daemon=False)
    t2.start()
    print("main thread start ....")
    t1.setName("Job1")
    t2.setName("Job2")
    print(t1.getName())
    print(t2.getName())
    print(t1.isAlive())
    print(t2.isAlive())
    print("Stack size:",threading.stack_size())  # 线程堆栈大小，0，是可以修改的
    print(threading.current_thread())  # 得到当前线程的对象 <_MainThread(MainThread, started 17404)>
    print(threading.main_thread())  # 得主前线程的对象，<_MainThread(MainThread, started 17404)>
    print(threading.activeCount())  # 获取活跃的线程数，3
    print(threading.TIMEOUT_MAX)  # 获取线程的最大超时，4294967.0，这个参数是可以修改的
    print(threading.enumerate())  # 该函数返回一个列表，成员是正在运行的threading.Thread的实例对象，所以把这一行放在不同位置，得到的列表不一样
    print(threading.get_ident())
    print("main thread end ....")


def main2():
    t1 = threading.Thread(target=job1, daemon=True)
    t1.start()
    t2 = threading.Thread(target=job1)
    t2.setDaemon(True)  # 设置为守护线程，这个方法必须在start方法之前调用
    t2.start()
    print("main thread start ....")
    print(t1.getName())  # 每一个线程默认有一个Thread-n名称
    print(t2.getName())
    print("main thread end ....")


if __name__ == '__main__':
    main1()  # 没有设置为守护线程的情况下，即使主线程退出，进程也不退出，等到使用线程退出，进程才退出
    # main2()  # 设置为守护线程后，只要主线程退出，子线程即使没有执行完成，也会强制退出

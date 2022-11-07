import threading
import time


def add():
    global num1
    cond_lock.acquire()  # 加锁
    print('num1', num1)
    temp = num1
    time.sleep(0.01)
    num1 = temp + 1
    cond_lock.wait()   # 线程等待
    cond_lock.notify()  # 通知其他线程执行
    cond_lock.release()  # 解锁


def sub():
    global num2
    cond_lock.acquire()  # 加锁
    print('num2', num2)
    temp = num2
    time.sleep(0.01)
    num2 = temp - 1
    cond_lock.wait()   # 线程等待
    cond_lock.notify()  # 通知其他线程执行
    cond_lock.release()  # 解锁


if __name__ == '__main__':
    cond_lock = threading.Condition()  # Condition锁
    num1 = 0
    num2 = 100

    # 一边做加法，一边做减法
    for i in range(100):
        t1 = threading.Thread(target=add)
        t2 = threading.Thread(target=sub)
        t1.start()
        t2.start()
    time.sleep(5)
    print(num1, num2)

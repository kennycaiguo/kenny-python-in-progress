# multiprocessing是用来解决GIL锁的限制，它可以实现并行,它的效率比threading.Thread()高很多
import multiprocessing as mp
import threading as th
import time


def job(a, b):
    print("a:%s,b:%s" % (a, b))


def task(q):
    res = 0
    for i in range(10000000):
        res += i + i ** 2 + i ** 3
    q.put(res)


def normal_proc():
    res = 0
    for _ in range(2):
        for i in range(10000000):
            res += i + i ** 2 + i ** 3
    print('res=', res)


def multi_core():
    q = mp.Queue()  # multiprocessing也是有Queue的
    p1 = mp.Process(target=task, args=(q,))
    p2 = mp.Process(target=task, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("total", q.get() + q.get())


def multi_thread():
    q = mp.Queue()
    t1 = th.Thread(target=task, args=(q,))
    t2 = th.Thread(target=task, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t1.join()
    print("total", q.get() + q.get())


def do_process1():
    p = mp.Process(target=job, args=(1, 2))
    p.start()
    p.join()  # 和 threading.Tread()类似，Process对象也是有join方法的
    print("这是主线程")


def main():
    start = time.time()
    normal_proc()
    time1 = time.time() - start
    print("normal:", time1)  # normal: 7.584682464599609
    multi_thread()
    time2 = time.time() - time1
    print("multithread:", time2)  # multithread: 1667683194.829555
    multi_core()
    time3 = time.time() - time2
    print("multiprocessing:", time3)  # multiprocessing 16.00933003425598


if __name__ == '__main__':
    # do_process1()
    # multi_core()
    main()

import multiprocessing, time

"""
注意：如果需要在进程间使用队列来共享数据，是不能够使用queue.Queue的
必须使用multiprocessing.queues.Queue，也就是进程通信队列
"""


def proc(q):
    time.sleep(1)
    print("son process")
    q.put("hello")
    q.put("girls")


if __name__ == '__main__':
    q = multiprocessing.Queue()  # <class 'multiprocessing.queues.Queue'>
    print(type(q))
    p1 = multiprocessing.Process(target=proc, args=(q,))
    p1.start()
    print("main process")
    print(q.get())
    print(q.get())

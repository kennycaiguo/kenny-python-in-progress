import threading
import time
from queue import Queue

q = Queue()


def producer(name):
    count = 1
    while count <= 10:
        print("开始制作包子。。。")
        time.sleep(3)
        q.put(count)
        print("%s正在制作第%s个包子" % (name, count))
        count += 1
        print("包子做好了。。。")


def consumer(name):
    count = 1
    while count <= 10:
        time.sleep(5)
        if not q.empty():
            data = q.get()
            print("%s正在吃第%s个包子" % (name, data))
            # print("%s正在吃第%s个包子" % (name, count))
            # q.get()
            count += 1
            print("包子吃完了。。。")
        else:
            print("没有包子了，需要等待一些时间。。。")
        count += 1


def main():
    t1 = threading.Thread(target=producer, args=("厨师",))
    c1 = threading.Thread(target=consumer, args=("顾客1",))
    c2 = threading.Thread(target=consumer, args=("顾客2",))
    c3 = threading.Thread(target=consumer, args=("顾客3",))
    t1.start()
    c1.start()
    c2.start()
    c3.start()
    t1.join()
    c1.join()
    c2.join()
    c3.join()
    print("finished")


if __name__ == '__main__':
    main()

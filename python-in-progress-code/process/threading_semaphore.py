import threading
import time
"""
信号量的作用是控制在上锁后可以有几个线程操作共享资源，lock和condition只能是一个
使用信号量的前提是保证设置信号量后的操作不会搞乱共享资源，否则跟没有上锁是一样的，也就是说只有在特定场合才使用
"""

class TaskThread(threading.Thread):
    def run(self) -> None:
        if _lock.acquire():
            print(self.name)
            time.sleep(2)
            _lock.release()


if __name__ == '__main__':
    _lock = threading.Semaphore(5)  # 信号量的作用是控制在上锁后可以有几个线程操作共享资源，lock和condition只能是一个
    l = []
    for i in range(100):
        t = TaskThread()
        t.start()
        l.append(t)

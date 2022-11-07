import threading
import time


class Boss(threading.Thread):
    def run(self):
        print("今晚加班到22:00")
        _event.set()  # 将默认的False修改为true
        time.sleep(3)
        print("22:00,时间到，下班！")
        _event.set()  # 将默认的False修改为true


class Worker(threading.Thread):
    def run(self):
        _event.wait()  # 默认值是False，会一直等待直到有线程把它改为True
        print("不是吧，真命苦。。。")
        _event.clear()  # 清除设置过的状态，
        _event.wait()  # 重新等待
        print("万岁。。。。。。")


if __name__ == '__main__':
    _event = threading.Event()  # 可以控制哪个线程先走
    b = Boss()
    w = Worker()
    w.start()  # 有了_event对象后，即使这个线程先执行，它也必须等待直到有线程修改了_event
    b.start()

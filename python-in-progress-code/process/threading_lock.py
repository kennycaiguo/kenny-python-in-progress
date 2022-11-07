import threading
import sys, time

# 读锁
read_lock = threading.Lock()
# 写锁
write_lock = threading.Lock()

X = 0


def write_proc():
    global X, read_lock, write_lock
    for i in range(2, 10):
        write_lock.acquire()
        X = i
        read_lock.release()


def read_proc():
    global X, read_lock, write_lock
    while True:
        read_lock.acquire()
        print("X=", X)
        write_lock.release()


def starts_threads():
    read_lock.acquire()
    wd_th = threading.Thread(target=write_proc)
    wd_th.setDaemon(True)
    wd_th.start()
    rd_th = threading.Thread(target=read_proc)
    rd_th.setDaemon(True)
    rd_th.start()
    time.sleep(5)


if __name__ == '__main__':
    starts_threads()

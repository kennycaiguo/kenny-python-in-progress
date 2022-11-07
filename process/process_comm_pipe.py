import multiprocessing, time


def proc_send(p):  #
    time.sleep(1)
    print("process send")
    p.send("hello")
    p.send("girls")


def proc_recv(p):
    time.sleep(1)
    print("process send")
    print(p.recv())
    print(p.recv())


if __name__ == '__main__':
    p = multiprocessing.Pipe() # 这里返回的是一个元组包括管道的两个端，一个可以作为写端另外一个可以作为读端
    print(type(p))
    p1 = multiprocessing.Process(target=proc_send, args=(p[0],))  # 一个进程传入写端
    p1.start()
    p2 = multiprocessing.Process(target=proc_recv, args=(p[1],))  # 一个进程传入读端
    p2.start()
    print("main process")

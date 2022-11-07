import multiprocessing, time


def consumer(p, name):
    while True:
        try:
            data = p.recv()
            print("%s收到%s包子" % (name, data))
        except EOFError as e:
            print(e)
            p.close()
            break


def producer(p, seq):
    for i in seq:
        p.send(i)
        time.sleep(1)
    else:
        p.close()


if __name__ == '__main__':
    p = multiprocessing.Pipe()
    child = multiprocessing.Process(target=consumer, args=(p[0],"child"))
    # 子进程作为消费者
    child.start()
    seq = (i for i in range(10))
    # 主进程作为生产者
    producer(p[1],seq)
    p[0].close()
    p[1].close()
    print("进程间通信-管道-主进程")

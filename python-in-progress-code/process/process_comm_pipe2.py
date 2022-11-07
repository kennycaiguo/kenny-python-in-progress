import multiprocessing, time


def boyfriend(p):
    print("写信给我女朋友。。。")
    p.send("hola,mi amor,te quiero mucho...,estoy esperando...")
    time.sleep(3)
    # print("等待女朋友的回信")
    print("回信来了，内容是：",p.recv())


def girlfriend(p):
    print("等待男朋友的信。。。")
    time.sleep(2)
    print("信到了，内容是:", p.recv())
    # print("回信给我男朋友。。。")
    p.send("hola,mi amor,te amo much,un besito...")


if __name__ == '__main__':
    p = multiprocessing.Pipe()  # 这里返回的是一个元组包括管道的两个端，一个可以作为写端另外一个可以作为读端
    print(type(p))
    p1 = multiprocessing.Process(target=boyfriend, args=(p[0],))  # 一个进程传入写端
    p1.start()
    p2 = multiprocessing.Process(target=girlfriend, args=(p[1],))  # 一个进程传入读端
    p2.start()
    print("main process")

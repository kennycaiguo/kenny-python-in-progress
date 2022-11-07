import multiprocessing
import time


def music():
    print("begin to listen....", time.strftime("%X"))
    time.sleep(5)
    print("finished listen....", time.strftime("%X"))
    

def game():
    print("begin to play game....", time.strftime("%X"))
    time.sleep(5)
    print("finished play game....", time.strftime("%X"))


def main():
    p1 = multiprocessing.Process(target=music)
    # p1.daemon = True
    p1.start()  # 注意:开启进程是比较消耗资源的所以如果不调用join方法，总是主进程先执行完成，所以进程不能开太多否则影响性能
    p2 = multiprocessing.Process(target=game)
    # 进程没有setDaemon方法，它只有daemon属性
    # p2.daemon = True  # 开启进程是比较消耗资源的所以如果将一个进程设置为守护进程，它可能连执行的机会都没有就退出了
    p2.start()
    # print(p2.name)
    # p2.terminate()
    print(p2.is_alive())
    print(p2.pid)
    p1.join()  # join方法可以设置timeout参数
    p2.join()
    print("主进程。。。")


if __name__ == '__main__':
    main()

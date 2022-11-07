import multiprocessing
import time, os

"""
python中进程池的使用：
如果频繁去创建一个进程，然后销毁它，会导致性能下降。对于这种情况推荐的做法是事先创建一个进程池，在有任务达到时从进程池中取出一个进程来执行相关任务，
在任务完成后便归还回去。这样做可以复用部分已有进程资源，达到提升效率的作用。
在 mulitprocessing 模块中有一个 Pool 类可以帮助我们完成该任务
"""


def child_proc(args):
    print("子进程在运行...")
    time.sleep(5)
    print("子进程结束。。。")
    # return "hello:%s-%s" % (os.getpid(), args)


def cb(args):  # 回调函数是属于主进程的
    print("args:%s" % os.getpid())


def main1():
    print("main的pid：", os.getpid())
    pool = multiprocessing.Pool(5)  # 创建一个有5个进程的进程池
    for i in range(10):
        # 如果需要使用回调函数，回调函数需要有参数的，否则抛异常，当func执行完毕，主进程会调用回调函数，并且把func的返回值传递进去，如果func没有返回值，
        # 这个参数的值就是None
        pool.apply_async(func=child_proc, args=(i,), callback=cb)  # 还可以有回调函数，执行一次任务成功，就会执行回调函数
    pool.close()
    pool.join()


def get_square_val(d):
    return d ** 2


def main2():
    inputs = [i for i in range(20)]
    pool = multiprocessing.Pool(4)
    out = pool.map(get_square_val, inputs)
    pool.close()  # 不再加入元素,
    pool.join()  # 注意进程池比较特别的地方是：1，一定要执行close方法和join方法才会执行pool的方法，2.join方法一定要在close方法后面执行
    print("pool result", out)


if __name__ == '__main__':
    main1()
    # main2()

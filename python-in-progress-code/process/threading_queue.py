import queue

"""
python有4种队列：
1，先进先出队列 queue.Queue
2.后进先出队列  queue.LifoQueue
3.优先队列     queue.PriorityQueue
4.双向队列    queue.deque() 
"""


def Queue_demo():  # 先进先出队列
    q = queue.Queue()
    q.put("jack")
    q.put("mary")
    q.put("ben")  # 放不进数据也会阻塞
    print(q.qsize())  # 元素的个数 3
    print(q.empty())  # 是否是空的 False
    while True:
        print(q.get())  # 取不到数据会一直阻塞


def LifoQueue_demo():  # 先进先出队列
    q = queue.LifoQueue()
    q.put("jack")
    q.put("mary")
    q.put("ben")  # 放不进数据也会阻塞
    print(q.qsize())  # 元素的个数 3
    print(q.empty())  # 是否是空的 False
    while True:
        print(q.get())  # 取不到数据会一直阻塞


def PriorityQueue_demo():
    """
    这个队列操作的是元组
    一般取的时候按照从小到大的顺序
    数字越小优先级越高，优先级越高，就越先出列
    """
    q = queue.PriorityQueue()
    # q.put((3, "Mike"))
    # q.put((1, "Mary"))
    # q.put((2, "Jesse"))  # 元组的第一个元素按照数字或者字母从小到大排序但是不能混合,第二个就无所谓
    q.put(['b', 2])
    # q.put([3,'a'])  # 混合就会报错  '<' not supported between instances of 'int' and 'str'
    q.put(['a', "jack"])  # 混合就会报错  '<' not supported between instances of 'int' and 'str'
    q.put(['c', 1])
    print(q.empty())
    print(q.qsize())
    print(q.full())
    # while True:
    #     print(q.get())  # 取不到数据会一直阻塞
    for i in range(q.qsize()):
        print(q.get())


if __name__ == '__main__':
    # Queue_demo()
    # LifoQueue_demo()
    PriorityQueue_demo()

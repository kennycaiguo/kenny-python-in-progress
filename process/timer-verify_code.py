import threading
from threading import Timer
import time
import random

"""
定时器生成验证码
"""


# 定义一个能生成验证码并且验证的类
class Verify_Code(object):
    # 加载生成的验证码,控制一个时间间隔后重新生成验证码
    def __init__(self):
        self.make_cache()  # 创建对象后马上生成验证码缓存

    def make_cache(self, seconds=10):  # 缓存验证码
        self.cache = self.make_code()
        print("验证码:", self.cache)
        self.t1 = Timer(seconds, self.make_cache)
        self.t1.start()

    def make_cache2(self):  # 当用户输入验证码错误，需要马上生成新的验证码
        self.cache = self.make_code()
        print("验证码:", self.cache)

    # 生成验证码
    def make_code(self,n=4):
        res = ''
        # print("".join(random.choices([s1,s2],k=4)))
        for i in range(n):
            s1 = str(random.randint(0, 9))
            s2 = chr(random.randint(65, 90))
            res += random.choice([s1, s2])
        return res

    # 验证方法
    def check(self):
        while True:
            yzm = input("请输入验证码>>:").strip()  # 去除空格
            if not yzm: continue
            if yzm.upper() == self.cache:
                print("恭喜，验证码通过")
                self.t1.cancel()  # 取消定时器执行
                break
            else:
                print("验证码错误！")
                self.make_cache2()


if __name__ == '__main__':
    c = Verify_Code()
    c.check()

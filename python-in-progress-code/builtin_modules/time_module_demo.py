import time
import datetime

"""
Time模块包含了一下内置的函数，既有时间处理的，也有转换时间格式的：

序号  函数及描述
1   time.altzone
　　　　　　返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
2   time.asctime([tupletime])
　　　　　　接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
3   time.clock( )
　　　　　　用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
4   time.ctime([secs])
　　　　　　作用相当于asctime(localtime(secs))，未给参数相当于asctime()
5   time.gmtime([secs])
　　　　　　接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
6   time.localtime([secs])
　　　　　　接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
7   time.mktime(tupletime)
　　　　　　接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。
8   time.sleep(secs)
　　　　　　推迟调用线程的运行，secs指秒数。
9   time.strftime(fmt[,tupletime])
　　　　　　接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
10  time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
　　　　　　根据fmt的格式把一个时间字符串解析为时间元组。
11  time.time( )
　　　　　　返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
12  time.tzset()  # 这个会报错
　　　　　　根据环境变量TZ重新初始化时间相关设置。
"""


def time_demo1():
    print(time.timezone)  # 21600
    print(time.asctime(datetime.datetime.now().timetuple()))  # Fri Oct 28 16:12:14 2022
    print(time.asctime())  # Fri Oct 28 16:12:14 2022,可以不传递参数的
    print(time.clock())  # 2e-07
    print(time.ctime(1000000000))  # Sat Sep  8 19:46:40 2001
    print(time.ctime())  # Fri Oct 28 16:16:55 2022 可以不传递参数的
    print(time.gmtime(999999999))  # time.struct_time(tm_year=2001, tm_mon=9, tm_mday=9, tm_hour=1, tm_min=46, tm_sec=39, tm_wday=6, tm_yday=252, tm_isdst=0)
    print(time.gmtime())  # time.struct_time(tm_year=2022, tm_mon=10, tm_mday=28, tm_hour=22, tm_min=24, tm_sec=55, tm_wday=4, tm_yday=301, tm_isdst=0)
    print(time.localtime()) # time.struct_time(tm_year=2022, tm_mon=10, tm_mday=28, tm_hour=16, tm_min=25, tm_sec=31, tm_wday=4, tm_yday=301, tm_isdst=0)
    print(time.mktime(time.localtime()))  # 1666996005.0
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))  # 2022-10-28 16:29:00,需要两个参数
    print(time.strptime('2019-12-26 03:12:20','%Y-%m-%d %H:%M:%S'))  # time.struct_time(tm_year=2019, tm_mon=12, tm_mday=26, tm_hour=3, tm_min=12, tm_sec=20, tm_wday=3, tm_yday=360, tm_isdst=-1)
    # print(time.tzset())  # 有问题，他说没有这个属性

if __name__ == '__main__':
    time_demo1()

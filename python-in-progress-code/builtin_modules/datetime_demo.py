import datetime
import time

"""
（一）、datetime模块中包含如下类：
类名	功能说明
date	日期对象,常用的属性有year, month, day
time	时间对象
datetime	日期时间对象,常用的属性有hour, minute, second, microsecond
datetime_CAPI	日期时间对象C语言接口
timedelta	时间间隔，即两个时间点之间的长度
tzinfo	时区信息对象
（二）、datetime模块中包含的常量
常量	功能说明	用法	返回值
MAXYEAR	返回能表示的最大年份	datetime.MAXYEAR	9999
MINYEAR	返回能表示的最小年份	datetime.MINYEAR	1
对象中包含的方法与属性
1、用于日期比较大小的方法
方法名	方法说明	用法
__eq__(…)	等于(x==y)	x.__eq__(y)
__ge__(…)	大于等于(x>=y)	x.__ge__(y)
__gt__(…)	大于(x>y)	x.__gt__(y)
__le__(…)	小于等于(x<=y)	x.__le__(y)
__lt__(…)	小于(x	x.__lt__(y)
__ne__(…)	不等于(x!=y)	x.__ne__(y)
以上方法的返回值为True\False
使用__sub__(...)和__rsub__(...)方法，其实二个方法差不太多，一个是正向操作，一个是反向操作：

方法名	方法说明	用法
__sub__(…)	x - y	x.__sub__(y)
__rsub__(…)	y - x	x.__rsub__(y)
"""


def datetime_date_demo1():
    _date = datetime.date.today()  # 日期对象是date类的实例，有年月日组成
    print(_date)  # 2022-10-28
    print(_date.year)  # 2022
    print(_date.month)  # 10
    print(_date.day)  # 28
    # 比较函数
    d1 = datetime.date(2018, 2, 2)
    d2 = datetime.date(2018, 11, 2)
    print(d1.__eq__(d2))  # 判断d1和d2是否相等     False
    print(d1.__ge__(d2))  # 判断d1是否大于或等于d2  False
    print(d1.__gt__(d2))  # 判断d1是否大于d2       False
    print(d1.__le__(d2))  # 判断d1是否小于或等于d2  True
    print(d1.__lt__(d2))  # 判断d1是否小于d2       True
    print(d1.__ne__(d2))  # 判断d1和d2是否不相等    True
    # 获得二个日期相差多少天
    print(d1.__sub__(d2))  # -273 days, 0:00:00
    print(d1.__sub__(d2).days)  # -273
    print(d1.__rsub__(d2))  # 273 days, 0:00:00
    print(d1.__rsub__(d2).days)  # 273


def datetime_date_demo_isoformat():
    d = datetime.date(2019, 2, 12)
    # 1).* isocalendar(...)*:返回一个包含三个值的元组，三个值依次为：year年份，week number周数，weekday星期数
    print(d.isocalendar())  # (2019, 7, 2)
    print(d.isocalendar()[0])  # 2019
    print(d.isocalendar()[1])  # 7
    print(d.isocalendar()[2])  # 2
    # 2). isoformat(...): 返回符合ISO 8601标准 (YYYY-MM-DD) 的日期字符串；
    print(d.isoformat())  # 2019-02-12
    # 3). isoweekday(...): 返回符合ISO标准的指定日期所在的星期数（周一为1…周日为7)
    print(d.isoweekday())  # 2
    # 4).与isoweekday(...)相似的还有一个weekday(...)方法，只不过是weekday(...)方法返回的周一为 0, 周日为 6
    print(d.weekday())  # 1


def datetime_date_convert_demo():
    # 1). timetuple(...):该方法为了兼容time.localtime(...)返回一个类型为time.struct_time的数组，但有关时间的部分元素值为0：
    a = datetime.date(2017, 3, 22)
    print(
        a.timetuple())  # time.struct_time(tm_year=2017, tm_mon=3, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=81, tm_isdst=-1)
    print(a.timetuple().tm_year)  # 2017
    print(a.timetuple().tm_mon)  # 3
    print(a.timetuple().tm_mday)  # 22

    # 2).toordinal(...)： 返回公元公历开始到现在的天数。公元1年1月1日为1
    print(a.toordinal())  # 736410
    # 3). replace(...)：返回一个替换指定日期字段的新date对象。参数3个可选参数，分别为year,month,day。注意替换是产生新对象，不影响原date对象
    print(a.replace(2019, 2, 1))  # 2019-02-01
    # 4).resolution属性：date对象表示日期的最小单位。这里是天。
    print(datetime.date.resolution)  # 1 day, 0:00:00
    # 5).fromordinal(...)：将Gregorian日历时间转换为date对象；Gregorian Calendar ：一种日历表示方法，类似于我国的农历，西方国家使用比较多。
    print(a.fromordinal(a.toordinal()))  # 2017-03-22
    # 6).fromtimestamp(...)：根据给定的时间戮，返回一个date对象
    t_stamp = time.time()
    print(datetime.date.fromtimestamp(t_stamp))  # 2022-10-28
    # 7).today(...)：返回当前日期
    print(datetime.date.today())  # 2022-10-28
    # 8).max属性： date类能表示的最大的年、月、日的数值，min属性，date类能表示的最小的年、月、日的数值
    print(datetime.date.max)  # 9999-12-31
    print(datetime.date.min)  # 0001-01-01


def datetime_date_output_demo():
    d = datetime.date(2019, 2, 12)
    # 1、如果你想将日期对象转化为字符串对象的话，可以用到__format__(...)方法以指定格式进行日期输出：
    print(d.__format__("%Y-%m-%d"))  # 2019-02-12  %Y->2019 %y->19
    print(d.__format__("%y-%m-%d"))  # 19-02-12
    # 与此方法等价的方法为strftime(...)
    print(d.strftime('%Y/%m/%d'))  # 2019/02/12
    # 2、如果只是相简单的获得日期的字符串，则使用__str__(...)
    print(d)  # 2019-02-12,print函数会自动大于__str__方法
    # 3、如果想要获得ctime样式的格式请使用ctime(...):
    print(d.ctime())  # Tue Feb 12 00:00:00 2019


def datetime_time_demo1():
    # time类由hour小时、minute分钟、second秒、microsecond毫秒和tzinfo五部分组成
    t = datetime.time(14, 1, 30, 899)
    print(t)  # 14:01:30.000899
    print(t.hour)  # 14
    print(t.minute)  # 1
    print(t.second)  # 30
    print(t.microsecond)  # 899
    print(t.tzinfo)  # None


def datetime_time_compare_demo():
    # 比较时间大小 相关方法包括：__eq__(...), __ge__(...), __gt__(...), __le__(...), __lt__(...)， __ne__(...)
    t1 = datetime.time(14, 1, 30, 899)
    t2 = datetime.time(13, 1, 30, 899)
    print(t1.__eq__(t2))  # False
    print(t1.__ge__(t2))  # True
    print(t1.__gt__(t2))  # True
    print(t1.__le__(t2))  # False
    print(t1.__lt__(t2))  # False
    print(t1.__ne__(t2))  # True


def datetime_time_attrib():
    # 其他属性
    # 1）、max：最大的时间表示数值：
    print(datetime.time.max)  # 23:59:59.999999
    # 2）、min：最小的时间表示数值
    print(datetime.time.min)  # 00:00:00
    # 3）、resolution：时间间隔单位为分钟
    print(datetime.time.resolution)  # 0:00:00.000001


def datetime_time_output():
    t = datetime.time(14, 1, 30, 899)
    print(t.strftime('%H:%M:%S'))  # 14:01:30 注意这里是格式是大写字符小写会报错
    # 2、ISO标准输出
    # 如果要使输出的时间字符符合ISO标准，请使用isoformat(...):
    a = datetime.time(12, 20, 59, 899)
    print(a.isoformat())  # 12:20:59.000899
    # 3、如果只是相简单的获得时间的字符串，则使用__str__(...)
    a = datetime.time(12, 20, 59, 899)
    print(a.__str__())    # 12:20:59.000899

def detetime_demo1():
    # datetime类其实是可以看做是date类和time类的合体，其大部分的方法和属性都继承于这二个类，相关的操作方法请参阅，本文上面关于二个类的介绍。其数据构成也是由这二个类所有的属性所组成的。
    #  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    d = datetime.datetime.now()
    print(d)  # 2022-10-28 14:35:09.156853
    # 专属于datetime的方法和属性
    # 1、 date(…)：返回datetime对象的日期部分：
    d_date = d.date()
    print(d_date)  # 2022-10-28
    # 2.time(…)：返回datetime对象的时间部分：
    d_time = d.time()
    print(d_time)  # 14:35:09.156853
    # 3、utctimetuple(…)：返回UTC时间元组：
    print(d.utctimetuple())  # time.struct_time(tm_year=2022, tm_mon=10, tm_mday=28, tm_hour=14, tm_min=36, tm_sec=20, tm_wday=4, tm_yday=301, tm_isdst=0)
    # 4、combine(…)：将一个date对象和一个time对象合并生成一个datetime对象：
    print(datetime.datetime.combine(d_date,d_time))  # 2022-10-28 14:38:01.108202
    # 5、now(…)：返回当前日期时间的datetime对象：
    print(datetime.datetime.now())  # 2022-10-28 14:38:55.445823
    # 7、strptime(…)：根据string, format 2个参数，返回一个对应的datetime对象：
    print(datetime.datetime.strptime('2022-10-28 14:38','%Y-%m-%d %H:%M'))  # 2022-10-28 14:38:00
    # 8、utcfromtimestamp(…):UTC时间戳的datetime对象，时间戳值为time.time()：
    print(datetime.datetime.utcfromtimestamp(time.time()))  # 2022-10-28 20:42:55.629089

def timedelta_demo():

    """
    timedalte 有三个只读属性：

    timedelta.min：负数最大时间差，相当于  timedelta(-999999999)。
    timedelta.max：正数最大时间差，相当于  timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)。
    timedelta.resolution：两个时间的最小差值 相当于   timedelta(microseconds=1)。
    """
    print(datetime.timedelta.max)   # 999999999 days, 23:59:59.999999
    print(datetime.timedelta.min)   # -999999999 days, 0:00:00
    print(datetime.timedelta.resolution)   # 0:00:00.000001
    print('===================================')
    # timedelta 其实就是列表时间日期的差
    d1 = datetime.datetime(2008,12,20,3,22)
    d2 = datetime.datetime(2018,12,22,3,22)
    delta = d2 - d1
    print(delta,type(delta))  # 3654 days, 0:00:00 <class 'datetime.timedelta'>
    print(delta.days)   # 3654
    print(delta.seconds)  #0:00:00.000001
    print("_______________________________________________")
    print(delta.total_seconds())  # 将时间差全部转换为秒： 315705600.0
    # 时间加减 timedelta
    now = datetime.datetime.now()
    print(now + datetime.timedelta(days=4))  # 从现在算起4天后的时间: 2022-11-01 15:45:07.315975
    print(now - datetime.timedelta(days=1))  # 昨天：2022-10-27 15:56:04.471798
    print(now - datetime.timedelta(days=7))  # 7天前也就是一个星期前： 2022-10-21 15:58:40.978353
    print(now - datetime.timedelta(days=30))  # 30天前也就是一个月前：2022-09-28 15:59:40.222474

if __name__ == '__main__':
    # datetime_date_demo1()
    # datetime_date_demo_isoformat()
    # datetime_date_convert_demo()
    # datetime_date_output_demo()
    # datetime_time_demo1()
    # datetime_time_compare_demo()
    # datetime_time_attrib()
    # datetime_time_output()
    # detetime_demo1()
    timedelta_demo()

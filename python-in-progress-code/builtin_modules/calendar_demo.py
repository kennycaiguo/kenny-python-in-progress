import calendar


def calendar_demo1():
    """
    calendar.calendar(year,w=4,l=4,c=6,m=4)
    w表示个位天数相邻两天之间的间隔宽度(字符空格数)，默认是2，在1号和2号中间有两个字符的空格，
    在10号和11号之间是1个空格，(当然是不换行的时候)，同时当w是2时，周一至周日的英文缩写只有两个字母。w如果小于2，都是取默认值2，w如果大于2时，
    相邻两天的间隔也跟着增大，周一至周日的英文缩写为3个字母，当w到9时，周一至周日的英文不缩写，(最长的单词是9个字母)。

    l表示每一个周占用的行数，默认是1，如果是2，则第一周和第二周中间会空一行，以此类推。小于1时，取1。

    c表示并排的两个月之间的间隔宽度，默认是6。但是c不小于w。即当c值小于w时，c等于w。

    m表示并排展示多少个月。默认是3，显示一排3个月，会显示4排。我们可以设置大于等于1的数，最多就是一排展示完12个月。m等于0会报错，小于0不打印日历。

    默认情况下，一周的第一天(显示在最左边的)是星期一Monday。可以使用calendar.setfirstweekday(num)函数设置，给num传入0至6的整数，0到6依次表示
    星期一到星期日，传其他数报错。可以使用calendar.firstweekday()获取当前最左边的是星期几，返回值是0到6的整数。"""
    # 打印一年的日历
    # cal = calendar.calendar(2023,w=4,l=4,c=6,m=4)
    # print(cal)
    # 打印一个月的月历
    '''
      calendar.month(year, month, w=2, l=1)返回指定年和月的月历。

    w和l这两个参数和上面打印年历中的一样。
    
    calendar.prmonth(year, month, w=2, l=1)也是打印月历，相当于print(calendar.month(year, month, w=2, l=1)),打印完成不换行。
    
    calendar.monthcalendar(year,month)返回一个嵌套列表。每个子列表是一个星期的日期编号，在第一个周和最后一个周，如果不满7天，则补0，将子列表的长度补到7。
    
    calendar.monthrange(year,month)返回一个元组，元组中有两个整数。第一个表示这个月的1号是星期几，第二个表示这个月有多少天。
    '''
    print("month: \n", calendar.month(2019, 10, w=0, l=0))
    # calendar.prmonth(2019, 10, w=0, l=0)
    print("monthcalendar: ", calendar.monthcalendar(2019, 11))  # 返回这个月的星期列表
    # 返回两个数，这个月的第一天是星期几，这个月有多少天
    print("monthrange: ", calendar.monthrange(2019, 10))  # 返回一个这个月的第一天和最后一天的元组，
    print("===============================")
    # calendar模块其他方法
    # calendar.timegm(tupletime)接受一个时间元组，返回时间戳，时间元组的值依次表示年、月、日、时、分、秒。
    print(calendar.timegm((2020, 10, 1, 8, 30, 30)))  # 返回一个时间戳 1601541030
    #  calendar.weekday(year,month,day)返回传入的日期是星期几。
    print(calendar.weekday(2019, 7, 12))
    # isleap()判断一个年份是否是闰年
    print(calendar.isleap(2021))  # False
    print(calendar.isleap(2020))  # True

    # calendar.leapdays(start, end)返回start,end之间有多少个闰年，左闭右开区间
    print(calendar.leapdays(2018, 2022))  # 1


if __name__ == '__main__':
    calendar_demo1()

import time


class MyTime:

    def my_date(self):
        """
            获取当前时间
        :return: 返回当前时间 格式：2019-6-20 12:00:00
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def my_week(self):
        """
            获取当天是星期几
        :return:返回当天是星期几  返回类型 int
        """
        return time.localtime()[6] + 1

    def my_week_format(self):
        """
            获取当天是星期几
        :return:返回当天是星期几  例：星期日
        """
        return self.__get_format_week(time.localtime())

    def get_week_from_date(self, date):
        """
            根据日期求星期
        :param date: 日期，格式：“2019-06-20”
        :return: 返回星期几 例：星期日
        """
        tuple_date = time.strptime(date, "%Y-%m-%d")
        return self.__get_format_week(tuple_date)

    def __seconds(self, date01, date02):
        """
            返回2个日期之间相差的秒数
        :param date01:
        :param date02:
        :return:
        """
        date1 = time.strptime(date01, "%Y-%m-%d")
        date2 = time.strptime(date02, "%Y-%m-%d")
        seconds = time.mktime(date2) - time.mktime(date1)
        return seconds * -1 if seconds < 0 else seconds

    def days(self, date01, date02):
        """
            计算2个日期之间相隔多少天
        :param date01: 第一个日期
        :param date02: 第二个日期
        :return:返回天数
        """
        seconds = self.__seconds(date01, date02)
        return int(seconds / (24 * 60 * 60))

    def months(self, month01, month02):
        """
            计算2个月份之间相隔多少个月
        :param month01: 第一个月份
        :param month02: 第二个月份
        :return:返回月份
        """
        year01 = time.strptime(month01, "%Y-%m")[0]
        month01 = time.strptime(month01, "%Y-%m")[1]
        year02 = time.strptime(month02, "%Y-%m")[0]
        month02 = time.strptime(month02, "%Y-%m")[1]
        date1 = int(str(year01) + str(month01))
        date2 = int(str(year02) + str(month02))
        if date1 > date2:
            date1, date2 = date2, date1
            year01, year02 = year02, year01
            month01, month02 = month02, month01
        sum = 0
        for year in range(year01, year02):
            sum += 12
        return sum + month02 if month01 > month02 else sum + month02 - month01

    def __get_format_week(self, local_time):
        """
            根据传入的时间元组，返回星期
        :param local_time: 时间戳 ，例 ：
        :return:返回星期几 例：星期一
        """
        week = {1: "星期一", 2: "星期二", 3: "星期三", 4: "星期四", 5: "星期五", 6: "星期六", 7: "星期日"}
        return week[(local_time[6] + 1)]

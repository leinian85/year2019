import time


class Time:

    def get_format_datetime(self):
        """
            获取当前时间
        :return: 返回当前时间 格式：2019-6-20 12:00:00
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def get_week(self):
        """
            获取当天是星期几
        :return:返回当天是星期几  返回类型 int
        """
        return time.localtime()[6] + 1

    def __get_format_week(self, local_time):
        """
            根据传入的时间元组，返回星期
        :param local_time: 时间戳 ，例 ：
        :return:返回星期几 例：星期一
        """
        week = {1: "星期一", 2: "星期二", 3: "星期三", 4: "星期四", 5: "星期五", 6: "星期六", 7: "星期日"}
        return week[(local_time[6] + 1)]

    def get_localweek_format(self):
        return self.__get_format_week(time.localtime())

    def get_week_for_date(self, date):
        tuple_date = time.strptime(date, "%Y-%m-%d")
        return self.__get_format_week(tuple_date)

    def count_days(self,date):
        """
            根据出生日期，计算一共活了多少天
        :param date: 出生日期，格式 ： ”2019-06-20“
        :return: 返回天数
        """
        min_year = time.strptime(date, "%Y-%m-%d")[0]
        max_year = time.localtime()[0]
        sum = 0
        for year in range(min_year,max_year):
            sum += 365
        sum += time.localtime()[7]
        return sum

t1 = Time()

# print(t1.get_week_for_date("2019-10-20"))

# print(t1.get_localweek_format())
print(t1.count_days("1985-05-18"))

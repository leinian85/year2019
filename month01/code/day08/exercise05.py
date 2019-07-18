def get_days(year, month):
    """
    根据年份月份返回天数
    :param year: 年份
    :param month: 月份
    :return: 天数
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return "31天"
    elif month in (4, 6, 9, 11):
        return "30天"
    elif month == 2:
        if if_leap_year(year):
            return "29天"
        else:
            return "28天"
    else:
        return "输入有误！"


def if_leap_year(year):
    """
    判断是否是闰年
    :param year:年份
    :return: 是闰年返回True,否则返回False
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


print(get_days(2001, 2))

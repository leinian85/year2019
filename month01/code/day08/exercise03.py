def get_grade_for_mark(mark):
    """
    根据成绩计算等级
    :param mark: 成绩
    :return: 等级
    """
    if 90 < mark <= 100:
        return "优秀"
    elif 60 <= mark <= 90:
        return "良好"
    elif 0 <= mark < 60:
        return "不及格"
    else:
        return "输入有误"

print(get_grade_for_mark(90))

def estimate_parity(num01):
    return "奇数" if num01 % 2 else "偶数"
print(estimate_parity(11))
def each_unit_sum(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

print(each_unit_sum(45678))
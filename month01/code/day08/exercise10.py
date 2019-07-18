def sum(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

print(sum(1,2,99))
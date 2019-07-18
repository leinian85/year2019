def count_seconds(hour=0, minute=0, second=0):
    return hour * 60 * 60 + minute * 60 + second

print(count_seconds(1,10,34))
print(count_seconds(minute=10,second=34))
print(count_seconds(hour=10,second=34))
print(count_seconds(hour=10))
print(count_seconds(minute=10))
print(count_seconds(second=34))

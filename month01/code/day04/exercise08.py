sum = 0
for item in range(10,51):
    if item % 10 in (2,5,9):
        continue
    sum += item
print(sum)
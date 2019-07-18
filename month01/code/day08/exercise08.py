count_fun01 = 0
def print_ok():
    global count_fun01
    count_fun01 += 1
    print("OK")

print_ok()
print(count_fun01)
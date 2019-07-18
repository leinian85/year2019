import  os
a = 1
pid = os.fork()

if pid < 0:
    print("create process fail")
elif pid == 0:
    print("create an old process")
    a = 18629
else:
    print("create an new process")

print("test",a)

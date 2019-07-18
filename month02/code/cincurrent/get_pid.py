import  os
pid = os.fork()
if pid < 0 :
    print("Error!")
elif pid == 0 :
    print(os.getpid())
    print(os.getppid())
else:
    print(pid)
    print(os.getpid())

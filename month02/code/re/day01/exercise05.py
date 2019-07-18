import re

class Address:
    def __init__(self,file,str):
        self.__file = file
        self.__str = str

    def get_addr(self):
        flag = False
        with open(self.__file,"r") as f:
            s = r"\b"+self.__str+r"\b"
            for strs in f.readlines():
                find = re.findall(s,strs)
                if find:
                    if find[0] == self.__str:
                        flag = True
                        continue
                if flag:
                    addr = re.findall(r"[a-z0-9]{4}\.[a-z0-9]{4}\.[a-z0-9]{4}",strs)
                    if addr:
                        return addr[0]
            return "没有找到"


a = Address("exc.txt","TenGigE0/0/2/0")
print(a.get_addr())
a = Address("exc.txt","TenGigE0/0/2/0.49")
print(a.get_addr())
a = Address("exc.txt","MgmtEth0/RSP0/CPU0/1")
print(a.get_addr())
a = Address("exc.txt","MgmtEth0/RSP0/CPU0/0")
print(a.get_addr())
a = Address("exc.txt","BVI201")
print(a.get_addr())
a = Address("exc.txt","BVI2011111")
print(a.get_addr())


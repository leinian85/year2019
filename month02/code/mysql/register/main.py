from regist import Register
def main():
    print("*"*10)
    print("1.注册 2.登录")
    print("*"*10)
    str = input("请选择:")
    if str in ("1","2"):
        name = input("name:")
        password = input("password:")
        register = Register()
        if str == "1":
            if register.register(name,password):
                print("注册成功")
            else:
                print("注册失败")
        elif str=="2":
            if register.login(name,password):
                print("登录成功")
            else:
                print("登录失败")

if __name__ == '__main__':
    main()


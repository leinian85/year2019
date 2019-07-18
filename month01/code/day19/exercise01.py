def validate(func):
    def wrapper(*args, **kwargs):
        print("验证账号密码")
        func(*args, **kwargs)
    return wrapper

@validate
def deposit(money):
    print("存%d元钱"%money)

@validate
def withdraw(money,login_id,pwd):
    print("取%d元钱"%money,login_id,pwd)


deposit(10000)
withdraw(1000,101,123456)
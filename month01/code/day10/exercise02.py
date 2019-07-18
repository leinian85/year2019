class Wife:
    count = 0

    def __init__(self):
        Wife.count+=1

    @classmethod
    def print_count(cls):
        print(cls.count)

w01 = Wife()
w01 = Wife()
w01 = Wife()
Wife.print_count()
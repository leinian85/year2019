# day12作业
# 1. 三合一
# 2. 学生管理系统代码能看懂
# 3. 完成学生管理系统中，根据成绩升序显示的功能.
# 4. 穷尽一切手段，在互联网中搜索"封装"的相关资料.
#    并结合课堂所讲(理论/代码)，总结为面向对象答辩的内容.
# 5. (扩展)将面向过程的购物车，改为面向对象的购物车.
"""
1.商品类：
    id,name,price,amount
2.商品控制类
    将商品信息读取然后返回
3.购物车类
4.购物车控制类
5.界面类：
"""


class Merchandise:
    def __init__(self, id="000", name="", price=0, amount=0):
        """
            商品变量
        :param id:商品编号
        :param name:商品名称
        :param price:商品价格
        :param amount:商品数量
        """
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, values):
        self.__id = values

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, values):
        self.__name = values

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, values):
        self.__price = values

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, values):
        self.__amount = values


class MerchandiseController:
    # __Merchandise_list = []

    def __init__(self):
        self.__Merchandise_list = []

    @property
    def Merchandise_list(self):
        return self.__Merchandise_list

    @Merchandise_list.setter
    def Merchandise_list(self, dict_merchandise):
        for k, v in dict_merchandise.items():
            me = Merchandise()
            me.id = k
            me.name = v["name"]
            me.price = v["price"]
            me.amount = v["amount"]
            self.__Merchandise_list.append(me)

    def print_merchandise_list(self):
        for item in self.Merchandise_list:
            print("编号:%s 名称:%s 单价:%d 库存:%d" % (item.id, item.name, item.price, item.amount))


class MerchandiseView:
    def __init__(self):
        self.__me = MerchandiseController()
        self.__me.Merchandise_list = dict_commodity_info
        self.__list_order = []

    def __show(self):
        while True:
            select = input("1键购买，2键结算")
            if select == "1":
                self.__buy()
            elif select == "2":
                self.__settlement()

    def __buy(self):
        self.__me.print_merchandise_list()
        self.__creat_order()
        print("添加到购物车。")

    def __creat_order(self):
        """
            创建订单
        """
        cid = self.__input_commodity_id()
        count = int(input("请输入购买数量："))
        order = {"cid": cid, "count": count}
        self.__list_order.append(order)
        for item in self.__me.Merchandise_list:
            if item.id == cid:
                item.amount -= count
                break

    def __input_commodity_id(self):
        """
            获取商品订单
        """
        while True:
            cid = input("请输入商品编号：")
            for item in self.__me.Merchandise_list:
                if item.id == cid:
                    return cid
            print("该商品不存在")

    def __settlement(self):
        """
            结算
        """
        total_price = self.__get_orders_and_total_price()
        self.__paying(total_price)

    def __paying(self, total_price):
        """
            支付过程
        :param total_price: 需要支付的价格
        """
        while True:
            money = float(input("总价%d元，请输入金额：" % total_price))
            if money >= total_price:
                print("购买成功，找回：%d元。" % (money - total_price))
                self.__list_order.clear()
                break
            else:
                print("金额不足.")

    def __get_orders_and_total_price(self):
        """
            打印订单
        """
        total_price = 0
        for item in self.__list_order:
            for item_list in self.__me.Merchandise_list:
                if item.cid == item_list.id:
                    print("商品：%s，单价：%d,数量:%d." % (item_list.name, item_list.price, item.count))
                    total_price += item_list.price * item.count
        return total_price

    def main(self):
        self.__show()


dict_commodity_info = {
    "101": {"name": "屠龙刀", "price": 10000, "amount": 10},
    "102": {"name": "倚天剑", "price": 10000, "amount": 10},
    "103": {"name": "九阴白骨爪", "price": 8000, "amount": 10},
    "104": {"name": "九阳神功", "price": 9000, "amount": 10},
    "105": {"name": "降龙十八掌", "price": 8000, "amount": 10},
    "106": {"name": "乾坤大挪移", "price": 10000, "amount": 10}
}

view = MerchandiseView()
view.main()

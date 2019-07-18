import random
import model


class DoubleClearContorl:
    def __init__(self, difficult, size):
        difficulty = model.DifficultyModel()
        self.__difficulty = difficulty
        self.__size = size
        self.__dict_map = {}
        self.__map_info = []
        self.__init_map_dict_info()
        self.map = []
        if difficult == difficulty.EASY:
            self.__getmap()
        else:
            self.__getmap_hard()
        self.__init_map()

    def __init_map_dict_info(self):
        """
        从配置文件读取地图中要显示的内容,写入字典中
        """
        with open("config", "r") as f:
            for line in f:
                str_line = line.split(" ")
                self.__dict_map[int(str_line[0])] = str_line[1].strip()

    def __getmap(self):
        """
        产生地图中需要用到的元素
        """
        num = int(self.__size ** 2 / 2)
        for i in range(0, num):
            self.__map_info.append(self.__dict_map[random.randint(1, 10)])

    def __getmap_hard(self):
        """
        产生地图中需要用到的元素
        """
        num = int(self.__size ** 2 / 2)
        for i in range(0, num):
            self.__map_info.append(self.__dict_map[random.randint(1, 26)])

    def __init_map(self):
        """
        地图初始化
        """
        map_info_tmp = self.__map_info.copy()
        for r in range(self.__size):
            list_tmp = []
            for c in range(self.__size):
                if len(map_info_tmp) == 0:
                    map_info_tmp = self.__map_info.copy()
                index = random.randint(0, len(map_info_tmp) - 1)
                list_tmp.append(map_info_tmp[index])
                del map_info_tmp[index]
            self.map.append(list_tmp)

    def __left(self, x, y, n):
        for i in range(1, n + 1):
            if self.transition(x - i, y) != "0":
                return False
        return True

    def __right(self, x, y, n):
        for i in range(1, n + 1):
            if self.transition(x + i, y) != "0":
                return False
        return True

    def __up(self, x, y, n):
        for i in range(1, n + 1):
            if self.transition(x, y + i) != "0":
                return False
        return True

    def __down(self, x, y, n):
        for i in range(1, n + 1):
            if self.transition(x, y - i) != "0":
                return False
        return True

    def transition(self, x, y):
        tmp_x = self.__get_x(y)
        tmp_y = self.__get_y(x)
        return self.map[tmp_x][tmp_y]

    def __get_x(self, y):
        return self.__size - 1 - y

    def __get_y(self, x):
        return x
    '''
    00(03) 01(13) 02(23) 03(33)
    10(02) 11(12) 12(22) 13(32)
    20(01) 21(11) 22(21) 23(31)
    30(00) 31(10) 32(20) 33(30)
    '''

    def __turn_xy(self, x1, y1, x2, y2):
        return (self.__get_x(y1), self.__get_y(x1), self.__get_x(y2), self.__get_y(x2))

    def is_clear(self, x1, y1, x2, y2):
        """
        判断2个坐标之间3步之内是否无阻挡
        :param x1: 第一个数的X轴
        :param y1: 第一个数的Y轴
        :param x2: 第二个数的X轴
        :param y2: 第二个数的Y轴
        :return:无阻挡返回 True ,否则返回 False
        """
        if x1 <= x2:
            min_x = x1
            min_y = y1
            max_x = x2
            max_y = y2
        else:
            min_x = x2
            min_y = y2
            max_x = x1
            max_y = y1

        new_max_y = min_y if max_y < min_y else max_y
        new_min_y = max_y if max_y < min_y else min_y

        # 以X轴较小的为准,向左移动,再以y轴较大的为准,向下移动
        for i in range(min_x, -1, -1):
            if self.__left(min_x, min_y, min_x - i):
                if self.__left(max_x, max_y, max_x - i):
                    if self.__down(i, new_max_y, new_max_y - 1 - new_min_y):
                        return True
                else:
                    continue
            else:
                break

        # 以X轴较大的为准,向右移动,再以y轴较大的为准,向下移动
        for i in range(max_x, self.__size):
            if self.__right(max_x, max_y, i - max_x):
                if self.__right(min_x, min_y, i - min_x):
                    if self.__down(i, new_max_y, new_max_y - 1 - new_min_y):
                        return True
                else:
                    continue
            else:
                break

        # 以X轴较小的为准,向X轴较大的移动,再以y轴较大的为准,向下移动
        for i in range(min_x, max_x + 1):
            if self.__right(min_x, min_y, i - min_x):
                if self.__left(max_x, max_y, max_x - i):
                    if self.__down(i, new_max_y, new_max_y - 1 - new_min_y):
                        return True
                else:
                    continue
            else:
                break

        if y1 <= y2:
            min_x = x1
            min_y = y1
            max_x = x2
            max_y = y2
        else:
            min_x = x2
            min_y = y2
            max_x = x1
            max_y = y1

        new_max_x = min_x if max_x < min_x else max_x
        new_min_x = max_x if max_x < min_x else min_x

        # 以y轴较大的为准,向上移动,再以x轴较大的为准,向左移动
        for i in range(max_y, self.__size):
            if self.__up(max_x, max_y, i - max_y):
                if self.__up(min_x, min_y, i - min_y):
                    if self.__left(new_max_x, i, new_max_x - 1 - new_min_x):
                        return True
                else:
                    continue
            else:
                break

        # 以y轴较小的为准,向下移动,再以x轴较大的为准,向左移动
        for i in range(min_y, -1, -1):
            if self.__down(min_x, min_y, min_y - i):
                if self.__down(max_x, max_y, max_y - i):
                    if self.__left(new_max_x, i, new_max_x - 1 - new_min_x):
                        return True
                else:
                    continue
            else:
                break

        # 以y轴较小的为准,向y轴较大的移动,再以x轴较大的为准,向左移动
        for i in range(min_y, max_y + 1):
            if self.__up(min_x, min_y, i - min_y):
                if self.__down(max_x, max_y, max_y - i):
                    if self.__left(new_max_x, i, new_max_x - 1 - new_min_x):
                        return True
                else:
                    continue
            else:
                break

        return False

    def clear(self, x1, y1, x2, y2):
        """
        清除地图中2个无阻挡的数据
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return:
        """
        result = self.__turn_xy(x1, y1, x2, y2)
        tmp_x1 = result[0]
        tmp_y1 = result[1]
        tmp_x2 = result[2]
        tmp_y2 = result[3]
        self.map[tmp_x1][tmp_y1] = "0"
        self.map[tmp_x2][tmp_y2] = "0"


if __name__ == "__main__":
    d = DoubleClearContorl("1", 8)
    d.map = [
        ["W", "E", "Z", "K", "E", "S", "S", "E"],
        ["Y", "W", "J", "0", "A", "0", "I", "Q"],
        ["M", "R", "I", "0", "0", "0", "J", "Z"],
        ["W", "D", "R", "0", "0", "A", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["A", "0", "0", "0", "A", "0", "0", "A"],
        ["0", "0", "0", "A", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "W"]
    ]
    # d.map = [
    #     ["0", "0", "E", "K"],
    #     ["0", "0", "W", "J"],
    #     ["0", "0", "0", "0"],
    #     ["K", "J", "E", "W"]
    # ]
    if d.is_clear(4, 2, 4, 6):
        d.clear(4, 2, 4, 6)
    else:
        print("不能消除")

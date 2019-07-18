import random
import os
import time
import bll


class DoubleClearView:
    def __init__(self, difficulty, size):
        self.__size = size
        self.__dbclear = bll.DoubleClearContorl(difficulty, size)

    def __draw_map(self):
        """
        画地图
        :return:
        """
        for i in range(self.__size - 1, -1, -1):
            print(i, end=" ")
            for item in self.__dbclear.map[self.__size - i - 1]:
                if item == '0':
                    print(" ", end=" ")
                else:
                    print(item, end=" ")
            print()

        for i in range(-1, self.__size):
            if i >= 0:
                print(i, end=" ")
            else:
                print(" ", end=" ")
        print()

    def __game_win(self):
        """
        判断游戏是否结束
        :return:胜利返回True
        """
        for line in self.__dbclear.map:
            for item in line:
                if item != "0":
                    return False
        return True

    def __get_coordinate(self):
        """
        获取坐标
        :return: 坐标正确返回 True 并返回坐标,坐标错误,返回 False 并返回错误信息
        """
        try:
            n, m = tuple(input("请输入坐标(以空格隔开):").split(" "))
            x1 = int(n[0])
            y1 = int(n[1])
            x2 = int(m[0])
            y2 = int(m[1])
            if (x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0
                    or x1 >= self.__size or x2 >= self.__size
                    or y1 >= self.__size or y2 >= self.__size):
                mag = "坐标超出范围,必须是0到%d之间!" % (self.__size - 1)
                return (False, mag)

            if self.__dbclear.transition(x1, y1) != self.__dbclear.transition(x2, y2):
                mag = "不是相同的字母,不能消除"
                return (False, mag)

            if x1 == x2 and y1 == y2:
                mag = "请输入2个不同的坐标"
                return (False, mag)

            return (True, x1, y1, x2, y2)
        except KeyboardInterrupt:
            exit()
        except ValueError:
            mag = "坐标格式不正确,请输入正确的格式!xy xy"
            return (False, mag)

    def __ganme_start(self):
        """
        开始游戏
        """
        while not self.__game_win():
            os.system("clear")
            self.__draw_map()
            coordinate = self.__get_coordinate()

            if coordinate[0]:
                x1 = coordinate[1]
                y1 = coordinate[2]
                x2 = coordinate[3]
                y2 = coordinate[4]

                if self.__dbclear.is_clear(x1, y1, x2, y2):
                    self.__dbclear.clear(x1, y1, x2, y2)
                else:
                    print("3步之内不能消除")
                    time.sleep(1)
            else:
                print(coordinate[1])
                time.sleep(1)
        else:
            os.system("clear")
            self.__draw_map()
            print("恭喜过关!")
            time.sleep(1)

    def main(self):
        self.__ganme_start()

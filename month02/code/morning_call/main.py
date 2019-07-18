import ui
import os
from model import DifficultyModel


def main():
    while True:
        try:
            os.system("clear")
            print("1.简单  2.困难  3.艰难")
            str = input("请选择难度:")
            Difficulty = DifficultyModel()
            if str not in Difficulty.difficulty:
                str = "1"
            Dbclearview = ui.DoubleClearView(str,Difficulty.difficulty[str])
            Dbclearview.main()
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()

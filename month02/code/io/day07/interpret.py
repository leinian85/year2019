class Interpret:
    @staticmethod
    def get_interpret(str01):
        file = open("../dict.txt", "r")
        for line in file:
            str02 = ""
            begin = 0
            for i in range(len(line)):
                if line[i] == " ":
                    str02 = line[:i]
                    begin = i
                    break
            if str02 > str01:
                return "没有找到该单词"
            elif str02 == str01:
                str03 = ""
                for i in range(begin,len(line)):
                    if line[i] != " ":
                        str03 = line[i:]
                        break
                return str03
        return "没有找到该单词"
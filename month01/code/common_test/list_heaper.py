class ListHeaper:
    @staticmethod
    def find_all(list_taget, condition):
        for item in list_taget:
            if condition(item):
                yield item

    @staticmethod
    def find_one(list_taget, condition):
        for item in list_taget:
            if condition(item):
                return item

    @staticmethod
    def count_self(list_taget, condition):
        count = 0
        for item in list_taget:
            if condition(item):
                count += 1
        return count

    @staticmethod
    def if_exist(list_taget, condition):
        for item in list_taget:
            if condition(item):
                return True
        return False

    @staticmethod
    def get_sum(list_taget,condition):
        sum = 0
        for item in list_taget:
            sum += condition(item)
        return sum

    @staticmethod
    def get_info(list_taget, condition):
        list01 = []
        for item in list_taget:
            list01.append(condition(item))
        return list01

    @staticmethod
    def max_value(list_taget, condition):
        max_value = 0
        for item in list_taget:
            if max_value < condition(item):
                max_value = condition(item)
        return max_value

    @staticmethod
    def sort_ascending(list_taget, condition):
        for i in range(len(list_taget)-1):
            for j in range(i+1,len(list_taget)):
                if condition(list_taget[i]) > condition(list_taget[j]):
                    list_taget[i],list_taget[j] = list_taget[j],list_taget[i]

    @staticmethod
    def min_value(list_taget, condition):
        min_value = list_taget[0]
        for i in range(1,len(list_taget)):
            if condition(min_value) > condition(list_taget[i]):
                min_value = list_taget[i]
        return min_value

    @staticmethod
    def fall(list_taget,condition):
        for r in range(len(list_taget)-1):
            for c in range(r+1,len(list_taget)):
                if condition(list_taget[r]) < condition(list_taget[c]):
                    list_taget[r],list_taget[c] = list_taget[c],list_taget[r]

    @staticmethod
    def my_remove(list_taget,condition):
        for i in range(len(list_taget)-1,-1,-1):
            if condition(list_taget[i]):
                del list_taget[i]

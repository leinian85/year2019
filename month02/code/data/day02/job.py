class LstackError(Exception):
    pass


class Data:
    def __init__(self, index, val):
        self.index = index
        self.val = val


class Node:
    """
    定义节点
    """

    def __init__(self, data, next=None):
        """
        :param data: 数据
        :param next: 下一个元素
        """
        self.data = data
        self.next = next


class LStack:
    """
    链表实现栈的功能
    """

    def __init__(self):
        """
        __top指向第一个元素
        """
        self.__top = None

    def is_empty(self):
        return self.__top is None

    def add(self, val):
        self.__top = Node(val, self.__top)

    def pop(self):
        if self.is_empty():
            raise LstackError("LStack is None")
        result = self.__top
        self.__top = self.__top.next
        return result

    def top(self):
        if self.is_empty():
            raise LstackError("LStack is None")
        return self.__top.val


class EstimateIntegrality:
    def is_matching(self, str):
        list01 = [[i, str[i]] for i in range(len(str))]
        lstack = LStack()
        dic_sign_in = {"(": ")", "[": "]", "{": "}"}
        dic_sign_out = {")": "(", "]": "[", "}": "{"}
        for item in list01:
            if item[1] in dic_sign_in:
                lstack.add(Data(item[0], item[1]))
            elif item[1] in dic_sign_out:
                if lstack.is_empty():
                    return (False, item[0])
                tmp = lstack.pop()
                if tmp.data.val != dic_sign_out[item[1]]:
                    return (False, tmp.data.index)
        if lstack.is_empty():
            return (True,None)


e1 = EstimateIntegrality()

# str01 = "nweb f[wfji) webf[iw(ebf)ui ninwequbfiwefifw enfjowe]n{fif wf}f"
# str01 = "a[{s]}]dfgh)jkl"
str01 = "a{[s]}d(fgh)jkl"
result = e1.is_matching(str01)
if not result[0]:
    print("第%d个位置不匹配" % (result[1] + 1))
else:
    print("全部匹配")

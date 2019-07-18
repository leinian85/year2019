class LstackError(Exception):
    pass

class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LStack:
    """
    链表实现栈的功能
    """
    def __init__(self):
        self.__top = None

    def is_empty(self):
        return self.__top is None

    def add(self,val):
        self.__top = Node(val,self.__top)

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

class Lalignment:
    """
    链表实现队列的功能
    """
    def __init__(self):
        self.top = None
        self.last = None

    def is_empty(self):
        return self.top is None

    def add(self,val):
        if self.is_empty():
            node = Node(val)
            self.top = node
            self.last = node
            return
        node = Node(val)
        self.last.next = node
        self.last = node

    def pop(self):
        if self.is_empty():
            raise LstackError("LStack is None!")
        result = self.top
        self.top = self.top.next
        return result

    def show(self):
        p = self.top
        while p is not None:
            print(p.val, end=" ")
            p = p.next
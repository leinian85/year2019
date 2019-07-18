"""
    linklist.py
    功能:实现单链表的构建和功能操作

"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = Node(None)

    def init_list(self, list_):
        p = self.head
        for item in list_:
            p.next = Node(item)
            p = p.next

    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val, end=" ")
            p = p.next

    def insert(self, index, node_):
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        node_.next = p.next
        p.next = node_

    def append(self, node_):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node_

    def delete(self, index):
        p = self.head
        for i in range(index):
            p = p.next
        t = p.next
        p.next = t.next

    def remove(self, value):
        p = self.head
        while p.next and p.next.val != value:
            p = p.next
        if not p.next:
            raise ValueError("%s is not in linklist" % value)
        else:
            p.next = p.next.next

    def is_empty(self):
        return self.head.next is None

    def clear(self):
        self.head.next = None

    def merge(self, LinkList):
        p = self.head
        while True:
            if p.next is None:
                break
            p = p.next
        p.next = LinkList.first()

    def first(self):
        return self.head.next

    def len(self):
        p = self.head
        i = 0
        while p.next is not None:
            p = p.next
            i += 1
        return i

    def order_by(self):
        max = self.len()
        r = 0
        while r < max:
            i = 0
            p = self.head
            while True:
                if p.next is None or p.next.next is None:
                    break
                if p.next.val > p.next.next.val:
                    n = p.next.next
                    self.delete(i + 1)
                    self.insert(i, n)
                p = p.next
                i += 1
            r += 1


l = LinkList()
l2 = LinkList()
# print(l.is_empty())
# l.insert(5, Node("leinian"))
# # l.append(Node("zhangsan"))
# # l.delete(2)
# # l.remove("leinian")
l.init_list([1, 13, 55, 7, 9])
l2.init_list([2, 4, 26, 18, 10, 51, 94, 40])
l.merge(l2)
l.order_by()
l.show()
# print(l3.len())
# node1 = Node(1)
# node2 = Node(2,node1)
# node3 = Node(3,node2)
#
# print(node2.next.val)

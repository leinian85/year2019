from link.link_all import Lalignment
class Node:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Btree:
    def pre_order(self,node):
        """
        先序
        """
        if node is None:
            return
        print(node.val,end= " ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self,node):
        """
        中序
        """
        if node is None:
            return
        self.in_order(node.left)
        print(node.val,end= " ")
        self.in_order(node.right)

    def psot_order(self,node):
        """
        后序
        """
        if node is None:
            return
        self.psot_order(node.left)
        self.psot_order(node.right)
        print(node.val,end= " ")

    def level_order(self,node):
        """
        层次遍历:注重思想,利用队列,先将根节入队,然后出队,每次出队的时候将左节点和右节点入队
        :param node:
        :return:
        """
        l1 = Lalignment()
        l1.add(node)





if __name__ == "__main__":
    f = Node("F")
    g = Node("G")
    i = Node("I")
    h = Node("H")
    d = Node("D",f,g)
    e = Node("E",i,h)
    c = Node("C",d,e)
    b = Node("B")
    a = Node("A",b,c)

bt = Btree()
bt.pre_order(a)
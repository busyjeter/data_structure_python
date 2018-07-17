# coding=utf-8
# before 3.4.2 单链表
import numpy


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        # 在表头添加
        self._head = LNode(elem, self._head)

    def pop(self):
        # 删除表头的结点
        if self._head is None:
            print("error")
        else:
            e = self._head.elem
            self._head = self._head.next
            return e

    def append(self, elem):
        # 在表尾添加
        if self._head is None:
            self._head = LNode(elem, self._head)
        # return    #如果这里用return，跳出if，就可以不用else
        else:
            p = self._head
            while p.next:
                p = p.next
            p.next = LNode(elem)

    def pop_last(self):
        # 删除最后一个结点
        if self._head is None:
            print("error")
        p = self._head
        # 只有一个元素
        if p.next is None:
            e = p.elem
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def filter(self, pred):
        p = self._head
        while p:  # 从P开始检索
            if pred(p.elem):
                yield (p.elem)
            p = p.next

    def printall(self):
        p = self._head
        while p:
            print(p.elem)
            p = p.next

    def for_each(self, proc):
        # Proc 的实参应该是可以作用于表元素的操作函数，
        # 它将被作用于每个表元素。
        p = self._head
        while p:
            proc(p.elem)
            p = p.next


# mlist=LList()
# for i in reversed(range(10)):
# 	mlist.prepend(i)
# for i in range(11,20):
# 	mlist.append(i)
# mlist.printall()
# print('---------')
# mlist.for_each(print)

class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        #  表头添加
        if self._head is None:  # 如果先检查self._head是否None，那么head就应该检查后再创建
            self._head = LNode(elem, self._head)
            self._rear = self._head  # 如果是空表就令表头=表尾
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):  # 表尾添加
        if self._head is None:  # 如果先检查self._head是否None，那么head就应该检查后再创建
            self._head = LNode(elem, self._head)
            self._rear = self._head  # 如果是空表就令表头=表尾
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop(self):
        # 删除表头的结点
        if self._head is None:
            print("error")
        else:
            e = self._head.elem
            self._head = self._head.next
            return e

    def pop_last(self):
        # 删除表尾结点
        if self._head is None:
            # 如果空表
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        e = self._rear.elem
        if p.next is None:  # 如果仅一个元素,判断后必须跳出函数，不然会执行下面while报错
            self._head = None  # 这里只能用head，因为统一用head的值来判断表空（eg之前的printall，head为None就不会输出）
            return e
        # 如果多于1个元素
        while p.next.next:
            p = p.next
        self._rear = p
        p.next = None
        return e


mlist = LList1()
mlist.prepend(10000)
for i in range(10):
    mlist.append(numpy.random.randint(1, 100))
mlist.printall()
print("----------")
print(mlist.pop_last())
print("----------")
mlist.printall()
# print("----------")


# for x in mlist.filter(lambda y: y%2==0):
# 	print (x)

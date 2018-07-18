# coding=utf-8


class LNode():
    def __init__(self, elem):
        self.elem = elem
        self._next = None


class LCList():
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):  # 前端插入
        p = LNode(elem)
        if self._rear is None:
            p._next = p
            self._rear = p
        else:
            p._next = self._rear._next
            self._rear._next = p

    def append(self, elem):  # 后端插入
        self.prepend(elem)
        self._rear = self._rear._next

    def pop(self):
        if self._rear is None:
            raise Exception
        e = self._rear._next.elem
        if self._rear._next==self._rear:
            self._rear=None
            return e
        else:
            self._rear._next = self._rear._next._next
            return e

    def pop_last(self):
        if self._rear is None:#空
            raise Exception
        e = self._rear.elem
        if self._rear._next==self._rear:#一个元素
            self._rear=None
            return e
        # elif self._rear._next._next == self._rear:#两个元素
        #     self._rear._next._next=self._rear._next
        #     return e
        else:#多于3个元素
            head=self._rear._next
            while head._next is not self._rear:
                head=head._next
            self._rear=head
            return e

    def printall(self):
        if self.is_empty():
            return
        p = self._rear._next
        while p is not self._rear:
            print(p.elem)
            p = p._next
        print(self._rear.elem)


mlist = LCList()
mlist.prepend(520)
for i in range(3):
    mlist.append(i)
mlist.printall()
print("---------")
print(mlist.pop())
print("---------")
print(mlist.pop_last())
print("---------")
mlist.printall()

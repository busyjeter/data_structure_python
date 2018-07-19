# coding=utf-8

class LNode():
    def __init__(self,elem,next_=None):
        self.elem=elem
        self._next=next_

class LList:#带有首尾结点引用的单链表
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

    def printall(self):
        p = self._head
        while p:
            print(p.elem)
            p = p._next

class DLNode(LNode):
    def __init__(self,elem,prev=None,next_=None):
        LNode.__init__(self,elem,next_)
        self._prev=prev

class DLList(LList):
    def __init__(self):
       LList.__init__(self)

    def prepend(self,elem):#前端插入
        p=DLNode(elem,None,self._head) #默认创建一个表头结点p（其中prev是None，见图3.14：表头的prev和表尾的next都是None）
        #另外这个表头结点p的next是原链表的head，即表示这个p希望加入原链表head前面
        if self._head is None:#以head判断 空表
            self._rear=p #head和rear都是p
        else:
            p._next._prev=p
        self._head=p #(或者和append一样)重要，因为给head指向结点P（空表的话，rear和head都指向p；非空表的话，前端插入p，再让P成为head）

    def append(self,elem):#后端插入
        p=DLNode(elem,self._rear,None)
        if self._head is None:
            self._rear=p
            self._head=p
        else:
            p._prev._next=p
            self._rear=p

    def pop(self):#  前端pop
        if self._head is None:
            raise Exception
        e=self._head.elem
        self._head=self._head._next
        if self._head is not None:#如果链表只有一个元素，上一行命令会使得self._head为None，然后下一行执行会报错：AttributeError: 'NoneType' object has no attribute '_prev'
            self._head._prev=None
        #这里可以不用像pop_last这样最后在rear=None时，同时设置head=None，是因为
        #判断是否empty通过head，这个pop判断一个元素后，head=None，因此就足以判断以后的empty了
        return e


    def pop_last(self):#  后端pop
        if self._head is None:
            raise Exception
        e=self._rear.elem
        self._rear=self._rear._prev#如果是一个元素，此时self._rear=None，
        if self._rear is None:
            self._head=None
        else:
            self._rear._next = None
        return e





mlist = DLList()
mlist.prepend(520)
for i in range(3):
    mlist.append(i)
mlist.prepend(520)
mlist.printall()
print("---------")
print(mlist.pop())
print("---------")
print(mlist.pop_last())
print("---------")
mlist.printall()
class LNode:
	def __init__(self,elem,next_=None):
		self.elem=elem
		self.next=next_

class LList:
	def __init__(self):
		self._head=None

	def is_empty(self):
		return self._head is None

	def prepend(self,elem):
		self._head=LNode(elem,self._head)

	def pop(self):
		#删除表头的结点
		if self._head == None:
			print("error")
		else:
			e=self._head.elem
			self._head=self._head.next
			return e

	def append(self,elem):
		if self._head==None:
			self._head=LNode(elem,self._head)
			# return    #不知道有什么用
		else:
			p=self._head
			while p.next:
				p=p.next
			p.next=LNode(elem)

	def pop_last(self):
		##删除最后一个结点
		if self._head ==None:
			print("error")
		p=self._head
		#只有一个元素
		if p.next==None:
			e=p.elem
			return e
		while p.next.next:
			p=p.next
		e=p.next.elem
		p.next=None
		return e

	def find(self):
		pass

	def printall(self):
		p=self._head
		while p:
			print(p.elem)
			p=p.next
	def for_each(self,proc):
		##Proc 的实参应该是可以作用于表元素的操作函数，
		##它将被作用于每个表元素。
		p=self._head
		while p:
			proc(p.elem)
			p=p.next

mlist=LList()
for i in reversed(range(10)):
	mlist.prepend(i)
for i in range(11,20):
	mlist.append(i)
mlist.printall()
print('---------')
mlist.for_each(print)






#仅有头结点引用的单链表

class LNode:
	def __init__(self,elem,next_=None):
		self.elem=elem
		self._next=next_

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
			self._head=self._head._next
			return e

	def append(self,elem):
		if self._head==None:
			self._head=LNode(elem,self._head)
			# return    #不知道有什么用
		else:
			p=self._head
			while p._next:
				p=p._next
			p._next=LNode(elem)

	def pop_last(self):
		##删除最后一个结点
		if self._head ==None:
			print("error")
		p=self._head
		#只有一个元素
		if p._next==None:
			e=p.elem
			return e
		while p._next._next:
			p=p._next
		e=p._next.elem
		p._next=None
		return e

	def find(self):
		pass

	def printall(self):
		p=self._head
		while p:
			print(p.elem)
			p=p._next


	def for_each(self, proc):
	##Proc 的实参应该是可以作用于表元素的操作函数，
	##它将被作用于每个表元素。
		p = self._head
		while p:
			proc(p.elem)
			p = p._next


	def rev(self):
		p = None
		while self._head is not None:
			q = self._head # 从head元素开始，取下head
			self._head = q._next  #，新head后移一个
			q._next = p # 取下的head 使得q.next=p=None ；通过循环不断滴把新链表添加
						# 在创造出来的结点q后面
			p = q #把创造出来的结点q作为新链表q的最后一个
		self._head = p #最后循环到取出原链表最后一个元素，创建出结点q，并把之前的链表p接在q.next，
						# 再把q赋值给P，此时P在最前面，因此赋值给head，成为新的链表

	def sort(self):
		if self._head is None:#empty
			raise Exception
		crt=self._head._next#从第二个结点开始处理
		while crt is not None: #如果只有一个元素 这个循环也不满足 直接完成工作（即不需要排序）
			x=crt.elem
			p=self._head
			while p is not crt and p.elem <=x:#跳过小元素直到p到达第一个比当前元素crt大的元素的位置
				p=p._next
			while p is not crt:#当p和crt还不重叠时
				y=p.elem
				p.elem=x
				x=y #交换遇到的第一个较大的元素elem
				p=p._next
			crt.elem=x #此时p和crt重叠，此时经过循环后，x最终的值=已排序的最后一个元素，再通过x赋值给crt，
			# 此时已完成crt.elem,即x=crt.elem的插入已排序段正确位置，而其他元素后移。
			crt=crt.next

	def sort2(self):
		# 这个最重要的是p，q，rem，head不同指针在同一链表上移动，插入
		p = self._head
		if p is None or p._next is None:
			# 如果空元素或者单元素，退出
			return
		rem = p._next  # 从第二个元素开始
		p._next = None  # 抽出第一个元素，和后面rem所指的元素比较
		while rem is not None:  # (循环1）
			p = self._head  # 每次循环开始让p从头开始寻找
			q = None  # q=None
			while p is not None and p.elem < rem.elem:  # （循环2）
				# 直到p所指元素更大或者到了末尾
				# p本来只有一个头元素，每次（循环1）结束，都会让p多一个元素，而且p和rem之间是已排好序的
				q = p
				p = p._next  # p,q不断在已排好序的链表中后移，直到不满足循环2：直到p所指元素更大或者到了末尾，
			# 此时把rem插入q,p之间（q是前一个元素，p是后一个元素）
			if q is None:  # 表头情况，说明循环2没执行，说明第一个头元素p就是最大的了
				# 链接拼接 交换头和次头
				self._head = rem  # 把rem移到head
				q = rem  # 此时q和head 都指向rem
				rem = rem._next
				q._next = p  # 小元素的下一个指向大元素
			else:  # 一般情况，rem插入q，p之间
				q._next = rem
				q = rem  # 因为q是临时用的，所以上一步用完q之后，q可以作为temp暂时指向rem，用于rem的拼接
				rem = rem._next
				q._next=p

			# q
			# self._head
			# p





mlist=LList()
for i in range(1,4):
	mlist.prepend(i)
# for i in range(11,20):
# 	mlist.append(i)
mlist.printall()
print('---------')
# mlist.rev()
mlist.sort2()
mlist.printall()
print('---------')
# mlist.for_each(print)






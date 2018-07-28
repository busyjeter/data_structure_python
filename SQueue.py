#基于python的list实现顺序表示的队列queue
class QueueUnderflow(ValueError):
	# print("hi error")
	pass
class SQueue():
	def __init__(self,init_len=8):
		self._len=init_len
		self._elems=[0]*self._len
		self._head=0
		self._num=0

	def is_empty(self):
		return self._num ==0

	def peek(self):
		if self.is_empty():
			raise QueueUnderflow()
		return self._elems[self._head]

	def dequeue(self):
		#head出队列
		if self.is_empty():
			raise QueueUnderflow("error in dequeue")
		e=self._elems[self._head]
		self._head=(self._head+1)%self._len
		self._num-=1
		return e

	def enqueue(self,elem):
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head+self._num)%self._len]=elem
		self._num+=1

	def __extend(self):
		old_len=self._len
		self._len*=2
		new_elems=[0]*self._len
		for i in range(old_len):
			new_elems[i]=self._elems[(self._head+i)%old_len]
		self._elems,self._head=new_elems,0

	def print_(self):
		print(self._elems)
		print("head is ",self._head)
		print("num is ",self._num)

sq=SQueue()
for i in range(1,7):
	sq.enqueue(i)
sq.print_()
print("----")
for i in range(1,7):
	print(sq.dequeue())
print("----")
sq.print_()
print("----")
for i in range(3):
	sq.enqueue(520)
sq.print_()


# jeterMBP:data_structure Jeter$ python3 SQueue.py 
# [1, 2, 3, 4, 5, 6, 0, 0]
# head is  0
# num is  6
# ----
# 1
# 2
# 3
# 4
# 5
# 6
# ----
# [1, 2, 3, 4, 5, 6, 0, 0]
# head is  6
# num is  0
# ----
# [520, 2, 3, 4, 5, 6, 520, 520]
# head is  6
# num is  3


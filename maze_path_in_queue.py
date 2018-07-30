class QueueUnderflow(ValueError):
	# print("hi error")
	pass


class SQueue():
	def __init__(self, init_len=8):
		self._len = init_len
		self._elems = [0] * self._len
		self._head = 0
		self._num = 0

	def is_empty(self):
		return self._num == 0

	def peek(self):
		if self.is_empty():
			raise QueueUnderflow()
		return self._elems[self._head]

	def dequeue(self):
		# head出队列
		if self.is_empty():
			raise QueueUnderflow("error in dequeue")
		e = self._elems[self._head]
		self._head = (self._head + 1) % self._len
		self._num -= 1
		return e

	def enqueue(self, elem):
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head + self._num) % self._len] = elem
		self._num += 1

	def __extend(self):
		old_len = self._len
		self._len *= 2
		new_elems = [0] * self._len
		for i in range(old_len):
			new_elems[i] = self._elems[(self._head + i) % old_len]
		self._elems, self._head = new_elems, 0

	def print_(self):
		print(self._elems)
		print("head is ", self._head)
		print("num is ", self._num)


def mark(maze, pos):
	maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
	if pos[0] < 0 or pos[1] < 0 or (pos[0] >= len(maze)) or (pos[1] >= len(maze[1])):
		return False
	return maze[pos[0]][pos[1]] == 0


def maze_solver_queue(maze, start, end):
	if start == end:
		print(start)
		return
	qu = SQueue()
	mark(maze, start)
	qu.enqueue(start)
	# temp = {}
	while not qu.is_empty():
		pos = qu.dequeue()
		for i in range(4):
			nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
			if passable(maze, nextp):
				if nextp == end:
					# temp[pos]=nextp
					print("find path")
					return
				mark(maze, nextp)
				# temp[pos] = nextp#如果这样的话，只会记录最后一次pos对应最新的nextp，
				#但是按理说要记录所有对应的
				qu.enqueue(nextp)
	print(temp)
	print("no path or all paths are trace")


start = (0, 0)
end = (3, 4)
maze = [[0, 1, 1, 0, 1], [0, 0, 0, 0, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
maze_solver_queue(maze, start, end)

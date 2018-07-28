class StackUnderflow(ValueError):
	pass
class SStack():
	#基于顺序表实现的栈类
	def __init__(self):
		self._elem=[]

	def is_empty(self):
		return self._elem==[]

	def top(self):
		if self.is_empty():
			raise StackUnderflow("in SStack.top()")
		return self._elem[-1]

	def push(self,elem):
		self._elem.append(elem)

	def pop(self):
		if self.is_empty():
			raise StackUnderflow("in pop()")
		return self._elem.pop()
	def print_all(self):
		return(self._elem)

def mark(maze,pos):
	maze[pos[0]][pos[1]]=2
def passable(maze,pos):
	if pos[0]<0 or pos[1]<0 or pos[0]>=len(maze[0]) or pos[1]>=len(maze[1]):
		return False
	return maze[pos[0]][pos[1]]==0

def print_path(end,pos,st):
		prev=st.print_all()
		for i in prev:
			print(i[0])

def maze_solver(maze,start,end):
	if start==end:
		print(start)
		return
	st=SStack()
	mark(maze,start)
	st.push((start,0))
	while not st.is_empty():
		pos,nxt=st.pop()
		for i in range(nxt,4):
			nextp=[pos[0]+dirs[i][0],pos[1]+dirs[i][1]]
			if nextp==end:
				st.push((pos,i))
				st.push((end,0))
				print_path(end,pos,st)
				return
			if passable(maze,nextp):
				st.push((pos,i+1))
				mark(maze,nextp)
				st.push((nextp,0))
				break#out of "for"
	print("no path")





start=[0,0]
end=[3,4]
maze=[[0,1,1,0,1],[0,0,0,0,0],[1,1,0,1,0],[0,0,0,0,0]]
dirs=((0, 1), (1, 0), (0, -1), (-1, 0))
maze_solver(maze,start,end)


#这个虽然迷宫有2个可能，但是永远只会输出一种因为47行的
#“for i in range(nxt,4):” 永远都是按照顺序来的，所有只能找到一种可能
# 除非我是随机？？但是怎么保存已经走过的路线呢？？ 
# [0, 0]
# [1, 0]
# [1, 1]
# [1, 2]
# [1, 3]
# [1, 4]
# [2, 4]
# [3, 4]













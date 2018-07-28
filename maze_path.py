#recursion
def mark(maze,pos):
	maze[pos[0]][pos[1]]=2
def passable(maze,pos):
	if pos[0]<0 or pos[1]<0 or pos[0]>=len(maze[0]) or pos[1]>=len(maze[1]):
		return False
	return maze[pos[0]][pos[1]]==0

def find_path(maze,pos,end):
	nextp=[0,0]
	mark(maze,pos)
	if pos==end:
		print(pos)
		return True
	for i in range(4):
		nextp[0]=pos[0]+dirs[i][0]
		nextp[1]=pos[1]+dirs[i][1]
		if passable(maze,nextp):
			if find_path(maze,nextp,end):
				print(pos)
				return True
	return False


pos=[0,0]
end=[3,4]
maze=[[0,1,1,0,1],[0,0,0,0,0],[1,1,0,1,0],[0,0,0,0,0]]
dirs=[(0, 1), (1, 0), (0, -1), (-1, 0)]

find_path(maze,pos,end)

# [3, 4]
# [3, 3]
# [3, 2]
# [2, 2]
# [1, 2]
# [1, 1]
# [1, 0]
# [0, 0]
# or
# [3, 4]
# [2, 4]
# [1, 4]
# [1, 3]
# [1, 2]
# [1, 1]
# [1, 0]
# [0, 0]
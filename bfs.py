class Algo():

	def __init__(self):
		# self.start_r = 0
		# self.start_r = 0
		# self.start_c = 0
		# self.end_r = 59
		# self.end_c = 59
		# self.col = 60
		# self.row = 60
		# self.walls = {}
		self.t1 = [1, 0, -1, 0]
		self.t2 = [0, 1, 0, -1]
		self.vis = [[False for j in range(34)]for i in range(22)]
		self.The_list = []
		# self.flag = False
		self.parent = {}
		# self.ways = [[False for j in range(60)]for i in range(60)]
		# self.dist = [[False for j in range(60)]for i in range(60)]

	def safe(self,r,c):
		if (r>=0 and r<22 and c>=0 and c<34):
			return True
		else:
			return False


	def bfs_util(self,maze,start_node,end_node):
		print(maze)
		r = start_node[0]
		c = start_node[1]
		end_r = end_node[0]
		end_c = end_node[1]
		q = []
		coor = str(r)+","+str(c)
		q.append(coor)

		while(len(q)>0):
			node = q[0]
			q.pop(0)
			var = node.split(",")
			r = int(var[0])
			c = int(var[1])
			
			for i in range(4):
				r0 = r + self.t1[i]
				c0 = c + self.t2[i]
				child = str(r0)+","+str(c0)
				if self.safe(r0, c0) is True:
					try:
						if (self.vis[r0][c0] is False and maze[r0][c0] is 0):
							self.parent[child] = node
							q.append(child)
							self.vis[r0][c0] = True
							self.The_list.append([r0, c0])
							if(r0 is end_r and c0 is end_c):
								return True

					except:
						print(r0, c0, ")))")
						print(self.maze[r0][c0])
						return

	def execute(self, maze, start_node, end_node):
		bb = False
		bb = self.bfs_util(maze, start_node, end_node)

		if(bb):
			print(self.The_list)
			print("************************************")
			print(self.parent)
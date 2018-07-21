def josephus(n,k,m):
	#n是人数，k是开始报数，m是第m个人报数退出
	people=list(range(1,n+1))
	num=n
	k1=k-1#第3个人开始,K=3,LIST[3-1]=3
	m1=m#数2个人
	while num>0:#当总人数大于0，进行循环
		count=0#计数器每次循环清零
		while count<m:
			if k1==n-1:#如果k1==最后一个数
				k1= -1
			while people[k1+1]==0:#如果下一个数==0，跳过，序号+1
				k1+=1
				if k1==n-1:#如果k1==最后一个数，从头开始
					k1= -1
			count+=1#如果下一个数非零，count+1
			k1+=1#序号+1
		print(people[k1],end="")#找出隔了m个人那个座位 ,end=""是在同一行输出
		people[k1]=0
		num-=1#存活人数-1
		#当最后只剩一个人的时候，循环2圈把自己数了2次 算2个人 
		#输出最后这个人
josephus(10,3,2)#57913610428










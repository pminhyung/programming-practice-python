import sys
n = int(sys.stdin.readline().rstrip())
stack=[]
for _ in range(n):
	comm = sys.stdin.readline().split()
	if len(comm)==1:
		if comm[0]=='pop':
			print(stack.pop()) if stack else print(-1)
		elif comm[0]=='size':
			print(len(stack))
		elif comm[0]=='empty':
			print(0) if stack else print(1)
		elif comm[0]=='top':
			print(stack[-1]) if stack else print(-1)
	else:
		stack.append(comm[1])
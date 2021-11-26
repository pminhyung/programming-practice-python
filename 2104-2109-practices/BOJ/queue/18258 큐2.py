from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
q=deque()
for _ in range(n):
	comm = sys.stdin.readline().split()
	if len(comm)==1:
		if comm[0]=='pop':
			print(q.popleft()) if q else print(-1)
		elif comm[0]=='size':
			print(len(q))
		elif comm[0]=='empty':
			print(0) if q else print(1)
		elif comm[0]=='back':
			print(q[-1]) if q else print(-1)
		elif comm[0]=='front':
			print(q[0]) if q else print(-1)
	else:
		q.append(comm[1])
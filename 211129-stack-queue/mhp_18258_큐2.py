import sys
from collections import deque
inp = sys.stdin.readline
n = int(inp().rstrip())
q = deque()

def run_command(comm):
	if comm[:len('push')] == 'push':
		_, num = comm.split()
		q.append(num)
	elif comm == 'pop':
		print(q.popleft()) if q else print(-1)
	elif comm == 'size':
		print(len(q))
	elif comm == 'front':
		print(q[0]) if q else print(-1)
	elif comm == 'back':
		print(q[-1]) if q else print(-1)
	elif comm == 'empty':
		print(0) if q else print(1)

for _ in range(n):
	comm = inp().rstrip()
	run_command(comm)
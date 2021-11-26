import sys
from collections import deque

n = int(sys.stdin.readline())
e = int(sys.stdin.readline())
g = [[] for _ in range(n+1)]

def bfs(v):
	visited=[]
	q = deque([v])
	while q:
		c = q.popleft()
		if c not in visited:
			q+=g[c]
			visited.append(c)
	return len(visited)-1

for _ in range(e):
	a,b = map(int, sys.stdin.readline().split())
	g[a].append(b)
	g[b].append(a)

print(bfs(1))
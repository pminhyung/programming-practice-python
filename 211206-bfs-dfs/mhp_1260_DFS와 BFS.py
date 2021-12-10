# 정점 번호가 작은 것을 먼저 방문 (sort)

# n,m,v
import sys
from collections import deque

inp = sys.stdin.readline
n, m, v =  map(int, inp().rstrip().split())

# graph 생성 [[], ...]
g = [[] for _ in range(n+1)] # dummy

for _ in range(m):
	a, b = map(int, inp().rstrip().split())
	g[a].append(b)
	g[b].append(a)

for i in range(n+1):
    g[i] = sorted(g[i])

# bfs 정의
def bfs(v):
    q = deque([v])
    res = []
    visited = [False for _ in range(n+1)] # dummy
    while q:
        curr = q.popleft()
        if not visited[curr]:
            q+=g[curr]
            visited[curr]=True
            res.append(str(curr))
    return res

# dfs 정의
def dfs(v):
    stack = [v]
    res = []
    visited = [False for _ in range(n+1)] # dummy
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            stack+=reversed(g[curr])
            visited[curr]=True
            res.append(str(curr))
    return res

# main : bfs, dfs 실행 (v)
print(' '.join(dfs(v)))
print(' '.join(bfs(v)))
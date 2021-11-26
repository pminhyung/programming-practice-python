# input 빠르게
import sys
input = sys.stdin.readline
from collections import deque

# dfs
def dfs(v):
    stack = [v]
    visited=[]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            stack+=reversed(graph[curr]) # 역순으로 넣어야 오름차순
            visited.append(curr)
    return visited

# bfs
def bfs(v):
    q = deque([v])
    visited = []
    while q:
        curr = q.popleft()
        if curr not in visited:
            q+=graph[curr]
            visited.append(curr)
    return visited

# n, m, v
n,m,v = map(int, input().split())

graph = [[] for _ in range(n+1)] # 0에 dummy 추가

# x,y
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i] = sorted(graph[i])

# traverse
print(' '.join(map(str, dfs(v))))
print(' '.join(map(str, bfs(v))))
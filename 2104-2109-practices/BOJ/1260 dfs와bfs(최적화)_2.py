# input 최적화
import sys
input = sys.stdin.readline # 괄호없이!!!
from collections import deque

# bfs와 dfs
def bfs(v):
    visited=[]
    q = deque([v])
    while q:
        curr =q.popleft()
        if curr not in visited:
            q+=graph[curr]
            visited.append(curr)
    return visited

def dfs(v):
    visited=[]
    stack = [v]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            stack+=reversed(graph[curr])
            visited.append(curr)
    return visited

# input 최적화
n,m,v = map(int, input().split())

# graph
graph = [[] for _ in range(n+1)] # 0은 dummy
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

# traverse
print(' '.join(map(str, dfs(v))))
print(' '.join(map(str, bfs(v))))
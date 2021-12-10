import sys
from collections import deque

inp = sys.stdin.readline

# n: 컴터수; m : 간선 수
n = int(inp().rstrip())
m = int(inp().rstrip())

# graph
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, inp().rstrip().split())
    g[a].append(b)
    g[b].append(a)

# bfs
def bfs():
    q = deque([1])
    cnt = 0
    visited = [False for _ in range(n+1)]
    while q:
        curr = q.popleft()
        cnt+=1
        visited[curr] = True
        for new in g[curr]:
            if not visited[new] and new not in q:
                q+=[new]
    return cnt

print(bfs()-1) # 1번 제외
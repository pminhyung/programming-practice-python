import sys
from collections import deque
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline().strip())
e = int(sys.stdin.readline().strip())
g = [0]+[[] for _ in range(n)]

visited=[]
def dfs(v):
    global visited
    q = deque([v])
    while q:
        curr = q.popleft()
        if curr not in visited:
            q+=deque(g[curr])
            visited.append(curr)
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

dfs(1)
print(len(visited)-1)
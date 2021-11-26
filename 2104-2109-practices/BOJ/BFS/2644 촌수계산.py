"""
형제간(0촌) 추가필요X
어차피 그 부모를 통해서 다시 내려와서 계산해야.
"""
import sys

n = int(sys.stdin.readline().rstrip())
t1, t2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().rstrip())

g = [False]+ [[] for _ in range(n)]
v = [False] * (n+1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    g[x].append(y)
    g[y].append(x)

from collections import deque

def	bfs(t1):
    q = deque([])
    q.append((t1, 0))
    while q:
        t, c = q.popleft()
        for near in g[t]:
            if near == t2:
                return c+1
            if not v[near]:
                q.append((near, c+1))
                v[near] = True
    return -1

print(bfs(t1))
"""
## 시간초과

not in visited -> visited[x] = True (순회 - 시간걸리므로)
deque += deque([i]) -> deque.append(i) (append가 훨씬빠르다)
"""

import sys
from collections import deque

def bfs(i):
    q = deque([i])
    visited=[False]*(n+1)
    visited[i]=True

    while q:
        c = q.popleft()

        for node in arr[c]:
            if not visited[node]:
                #q+=deque([i])
                q.append(node)
                visited[node]=True

    return sum(visited)

n,m = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    arr[b].append(a)

com =[]
max_=0
for i in range(1, n+1):
    cnt = bfs(i)
    if max_<cnt:
        com=[i]
        max_=cnt
    elif max_==cnt:
        com.append(i)

print(*com)
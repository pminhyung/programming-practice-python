"""
변수명 수정 시 다른부분도 수정 주의
int(input) 주의
"""
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
g = [[] for _ in range(n+1)]
par = [0]*(n+1)

for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    g[x].append(y)
    g[y].append(x)

def bfs():
    q = deque([])
    q.append(1)
    while q:
        parent = q.popleft()
        for child in g[parent]:
            if child!=par[parent]: # 자식노드만 추가
                q.append(child)
                par[child] = parent

bfs()

for i in range(2, n+1):
    print(par[i])
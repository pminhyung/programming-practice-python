"""
g[r][c]에 cnt를 기록하여, visited를 대신함 (g[nr][nc]==1 : not visited)
- 메모리 효율 증가
"""

import sys
from collections import deque

inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())
g = [list(map(int, inp().rstrip())) for _ in range(n)]

def bfs():
    q = deque([(0,0)]) # idx = (n-1, m-1)
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = dr[i]+r
            nc = dc[i]+c
            if 0<=nr<n and 0<=nc<m and g[nr][nc]==1:
                g[nr][nc]+=g[r][c]
                q+=[(nr,nc)]
    return g[n-1][m-1]

print(bfs())
"""
- m, n input 순서 조심
- nr, nc에 대해 visited 표시 X ->  append 조건식에 not in q 추가
"""

import sys
from collections import deque

inp = sys.stdin.readline

# bfs
def bfs(r,c):
    global g
    q = deque([(r,c)])
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    while q:
        r, c = q.popleft()
        # visited 표기
        g[r][c] = -1
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<=nc<m and g[nr][nc]==1 and (nr,nc) not in q :
                q+=[(nr,nc)]


# main (for + bfs)
T = int(inp().rstrip())
for _ in range(T):
    m, n, k = map(int, inp().rstrip().split())

    # arr
    g = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        X, Y = map(int, inp().rstrip().split())
        g[Y][X] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j]==1:
                bfs(i,j) # visited 표기용
                cnt+=1
    print(cnt)
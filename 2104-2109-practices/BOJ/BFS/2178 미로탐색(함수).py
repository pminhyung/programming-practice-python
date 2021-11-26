"""
bfs 함수화

- arg : 초기지점 (0,0)
- graph 목표지점(거리비용) return
"""

import sys
from collections import deque

# bfs
def bfs(x,y):

    # q
    q = deque([[x,y]])

    # while
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=m-1 and 0<=ny<=n-1:
                if arr[ny][nx]==1:
                    arr[ny][nx] = arr[y][x]+1
                    q+=[[nx,ny]]
    return arr[n-1][m-1]

# input
n, m =map(int,sys.stdin.readline().split())

# arr
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

# 방향
dx = [1,-1,0,0]
dy = [0,0,1,-1]

print(bfs(0,0))
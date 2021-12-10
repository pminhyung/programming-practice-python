# 대각선포함 : for _ in range(8)

import sys
inp = sys.stdin.readline

dr = [1, -1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, 1, -1, 1, 1, -1, -1]

def dfs(i,j):
    stack = [(i,j)]
    while stack:
        r,c  = stack.pop()
        g[r][c] = 0
        for i in range(8):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<h and 0<=nc<w and g[nr][nc]!=0 and (nr,nc) not in stack:
                stack.append((nr,nc))

while True:
    w, h = map(int, (inp().rstrip().split()))

    if (w,h)==(0,0):
        break
    
    g = [list(map(int, inp().rstrip().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if g[i][j]!=0:
                dfs(i, j)
                cnt += 1

    print(cnt)
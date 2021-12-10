"""
시간초과 : deepcopy 사용..
"""

import sys
#from copy import deepcopy

def dfs(i,j):
    stack = [(i,j)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while stack:
        r,c = stack.pop()
        visited[r][c] = 1
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<=nc<n and g[nr][nc]>h and visited[nr][nc]==0:
                stack.append((nr,nc))

inp = sys.stdin.readline
n = int(inp().rstrip())

g = []
max_val = 1
for _ in range(n):
    row_li = list(map(int, inp().rstrip().split()))
    max_val = max(max(row_li), max_val)
    g.append(row_li)

for h in range(0, max_val+1):
    if h == 0:
        max_cnt = 1
        continue
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)] # 방문 시 1
    for i in range(n):
        for j in range(n):
            if g[i][j]>h and visited[i][j]==0:
                dfs(i,j)
                cnt+=1
    max_cnt = max(cnt, max_cnt)
print(max_cnt)
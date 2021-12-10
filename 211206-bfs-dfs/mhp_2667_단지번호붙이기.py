"""
- 미로탐색과 달리 각 이웃에 대해 count를 달리 해야
- popleft 시 cnt+=1, visited 표시 : 이웃이 없을 경우 스스로 count 필요
- 따라서 nr, nc에 대해 visited 표시 X ->  append 조건식에 not in q 추가
"""

import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp().rstrip())
g = [list(map(int, inp().rstrip())) for _ in range(n)]

def bfs(r,c):
    global g
    q = deque([(r,c)])
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    cnt=0

    while q:
        r,c = q.popleft()
        g[r][c] = -1 # visited
        cnt+=1
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<=nc<n and g[nr][nc]==1 and ((nr,nc) not in q):
                q+=[(nr,nc)]
    return cnt

res = []
for i in range(n):
    for j in range(n):
        # 1이면 bfs 실행
        if g[i][j]==1:
            # 아파트 cnt -> res.append
            res.append(bfs(i,j))
print(len(res))  
print('\n'.join(map(str, sorted(res))))
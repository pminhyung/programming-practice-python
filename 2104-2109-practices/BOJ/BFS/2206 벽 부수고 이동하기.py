"""
# https://kyun2da.github.io/2020/09/22/breakWallandMove/
*** A지점 포함해서, 벽을 몇번 부쉈냐의 값을 3차원 배열 값으로 가지고 다녀야하는 문제
*** 3차원 배열 만드는 거 조심
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

if (n, m) == (0, 0):
    print(1)
    sys.exit()

g = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
limit = 2

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c, hasbroken):
    cost = [[[-1]*limit for _ in range(m)] for _ in range(n)]
    q = deque([])
    q.append((r, c, hasbroken))
    cost[r][c][hasbroken] = 1

    while q:
        r, c, hasbroken = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0<=nr<n) or not (0<=nc<m):
                continue

            # if (nr, nc) == (n-1, m-1):
            #     return cost[r][c][0], cost[r][c][1]


            if hasbroken==0: # 벽을 부순 적 없을 때
                if g[nr][nc]==0 and cost[nr][nc][hasbroken]==-1:  # 벽이 아닐 때, not visited
                    d = cost[r][c][hasbroken]
                    cost[nr][nc][hasbroken] = d+1
                    q.append((nr,nc,hasbroken))
                elif g[nr][nc]==1 and cost[nr][nc][hasbroken+1]==-1: # 벽일 때, not visited
                    d = cost[r][c][hasbroken]
                    cost[nr][nc][hasbroken+1] = d+1
                    q.append((nr,nc,hasbroken+1))
                continue

            # if hasbroken==1:  # 벽을 부순 적 없을 때
            #     if g[nr][nc]==0: # 벽이 아닐 때
            #         d = cost[r][c][hasbroken]
            #         cost[nr][nc][hasbroken] = d+1
            #         q.append((nr,nc,hasbroken))
            #     elif g[nr][nc]==1: # 벽일 때
            #         continue
            # 아래 문단으로 축약

            if hasbroken==1 and g[nr][nc]==0 and cost[nr][nc][hasbroken]==-1:
                # 벽을 부순 적 없을 때, 벽일 때, not visited
                d = cost[r][c][hasbroken]
                cost[nr][nc][hasbroken] = d+1
                q.append((nr,nc,hasbroken))

    return cost[n-1][m-1][0], cost[n-1][m-1][1]

ans1, ans2 = bfs(0,0,0)

if ans1==-1 and ans2==-1: # 둘다 -1
    print(-1)
elif ans1!=-1 and ans2!=-1: # 둘다 자연수, 도착점(+1)
    print(min(ans1, ans2))
else: # -1과 자연수
    print(max(ans1, ans2))

"""
반례
6 3
000
110
000
011
111
000
"""
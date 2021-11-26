"""
3차원 배열 사용, cost배열에 bfs의 일수 기입
*****bfs를 어떻게 돌릴것인가 매우 중요!

익은 토마토들에서 동시적으로 시작하여 bfs를 돌리는 것이 중요!
따라서 처음부터 전체 상자를 순회하며 bfs를 무작정 돌리면 하나의 익은 토마토 기준으로 다른 토마토들이 수정되어 오답

반례1
5 3 1
1 0 0 0 0 0
0 0 0 0 0 0
1 1 1 1 1 1
정답:2

반례2
10 2 1
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
정답:1
"""

import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
g = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
cost = [[[0]*m for _ in range(n)] for _ in range(h)]

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]


def bfs():
    global q
    while q:
        k, r, c = q.popleft()
        for i in range(6):
            nk = k + dk[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nk < h and 0 <= nr < n and 0 <= nc < m and g[nk][nr][nc] == 0 and cost[nk][nr][nc] == 0:
                # print(nr, nc)
                q.append((nk, nr, nc))
                g[nk][nr][nc] = 1
                cost[nk][nr][nc] = cost[k][r][c] + 1


# 아래의 경우 모든 익은토마토에서 날짜 계산이 동시에 이루어지지 않는다 (정답보다 증가한다)
# for k in range(h):
#     for r in range(n):
#         for c in range(m):
#             if g[k][r][c]==1 and cost[k][r][c]==0:
#                 # print(r,c)
#                 bfs(k, r, c)


# 처음 익은 토마토에서 bfs를 먼저 동시적으로 시작한다 - 중요!
# 익은토마토 list
q = deque([])
for k in range(h):
    for r in range(n):
        for c in range(m):
            if g[k][r][c]==1 and cost[k][r][c]==0:
                q.append((k, r, c))

# 익은 토마토 bfs
bfs()

# 안익은 토마토 존재시 -1 출력
for k in range(h):
    for r in range(n):
        for c in range(m):
            if g[k][r][c]==0:
                print(-1)
                sys.exit()

# 일수 최댓값(최소한 다 익는데 필요한 일수)
max_result = 0
for k in range(h):
    for r in range(n):
        max_result = max(max_result, max(cost[k][r]))

print(max_result)
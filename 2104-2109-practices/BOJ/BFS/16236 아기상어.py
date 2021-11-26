"""
- heapq를 이용 -> 거리, row, column 순의 최소 heap 사용
- 먹이를 주변에서 찾자마자 바로 먹는 것 X -> heapq에 넣고 우선순위로 나온 것을 먹음 (그래서 먹는 것에 대한 조건들을 for문 앞에서 처리)
- 먹이 먹은 후 거리(d)를 꼭 초기화 해야한다!!
"""
import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().rstrip())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for r in range(n):
    for c in range(n):
        if g[r][c] == 9:
            r0, c0 = r, c
            g[r][c] = 0
            break


def bfs(r, c):

    global g
    tot = 0
    size = 2
    state = 0
    v = [[False]*n for _ in range(n)]
    v[r][c] = True

    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]

    q = []
    heappush(q, (0, r, c))


    while q:
        d, r, c = heappop(q)

        # 먹이 존재
        if 0 < g[r][c] < size:
            g[r][c] = 0
            state += 1
            tot += d
            d = 0

            # 먹고 bfs 초기화
            q = []
            v = [[False] * n for _ in range(n)]

            # 사이즈업
            if state == size:
                size += 1
                state = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<n and 0<=nc<n and v[nr][nc]==False:
                # 먹이 없고 지나갈 수 있다면 경로추가
                if g[nr][nc]<=size:
                    v[nr][nc] = True
                    heappush(q, (d + 1, nr, nc))
    return tot

print(bfs(r0, c0))
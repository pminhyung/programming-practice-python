"""
대각선범위까지
dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, -1, 1, -1, 1]

# graph 순회
# 주변 9개에 육지 있으면 bfs로 추가
# v에 표시 (cnt+1)
"""

import sys
from collections import deque

while True:
    w, h = map(int, sys.stdin.readline().split())

    if (w, h) == (0, 0):
        break

    g = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]
    cnt = 0
    dr = [0, 0, 1, -1, 1, 1, -1, -1]
    dc = [1, -1, 0, 0, -1, 1, -1, 1]


    def bfs(r,c):
        q = deque([])
        q.append((r, c))
        while q:
            r, c = q.popleft()
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < h and 0 <= nc < w and g[nr][nc] == 1 and v[nr][nc] == False:
                    q.append((nr, nc))
                    v[nr][nc] = True

    for r in range(h):
        for c in range(w):
            if g[r][c] == 1 and v[r][c] == False:
                v[r][c] = True
                bfs(r,c)
                cnt += 1
    print(cnt)
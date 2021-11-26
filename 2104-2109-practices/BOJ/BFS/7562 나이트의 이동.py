"""
나이트 이동범위
dr = [2, 2, -2, -2, 1, -1, 1, -1]
dc = [1, -1, 1, -1, 2, 2, -2, -2]

r, c == nr, nc 순서주의!
"""
import sys
from collections import deque

dr = [2, 2, -2, -2, 1, -1, 1, -1]
dc = [1, -1, 1, -1, 2, 2, -2, -2]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    I = int(sys.stdin.readline().rstrip())
    src_c, src_r = map(int, sys.stdin.readline().split())
    tar_c, tar_r = map(int, sys.stdin.readline().split())

    if (src_c, src_r) == (tar_c, tar_r):
        print(0)
        continue

    g = [[0] * I for _ in range(I)]


    def bfs(src_r, src_c):
        q = deque([])
        q.append((src_r, src_c))
        while q:
            r, c = q.popleft()
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if (nr, nc) == (tar_r, tar_c):
                    return g[r][c] + 1

                if 0 <= nr < I and 0 <= nc < I and g[nr][nc] == 0:
                    q.append((nr, nc))
                    g[nr][nc] = g[r][c] + 1

    print(bfs(src_r, src_c))
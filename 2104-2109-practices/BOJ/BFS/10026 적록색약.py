"""
line62 continue 삽입 실수
bfs 2개 구현하면 되는 간단한 문제
"""
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
g = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# if n==1:
#     print(1, 1)
#     sys.exit()

normalv = [[0] * n for _ in range(n)]
v = [[0] * n for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs_normal(r, c):
    q = deque([])
    q.append((r, c))

    while q:
        r, c = q.popleft()
        color = g[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and g[nr][nc] == color and normalv[nr][nc] == False:
                q.append((nr, nc))
                normalv[nr][nc] = True


def bfs(r, c):
    q = deque([])
    q.append((r, c))

    while q:
        r, c = q.popleft()
        color = g[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if color in 'RG':
                if 0 <= nr < n and 0 <= nc < n and g[nr][nc] in 'RG' and v[nr][nc] == False:
                    q.append((nr, nc))
                    v[nr][nc] = True
            else:
                if 0 <= nr < n and 0 <= nc < n and g[nr][nc] == color and v[nr][nc] == False:
                    q.append((nr, nc))
                    v[nr][nc] = True

normal_cnt = 0
cnt = 0
for r in range(n):
    for c in range(n):
        if normalv[r][c] == False:
            bfs_normal(r, c)
            normal_cnt += 1

        if v[r][c] == False:
            bfs(r, c)
            cnt += 1

print(normal_cnt, cnt)
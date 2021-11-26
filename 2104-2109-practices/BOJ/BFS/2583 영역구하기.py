"""
나의실수:
- bfs 조건식에서 graph의 값이 0, 1 중 어느것을 추가하는지 확인
- r, c, nr, nc 잘 확인할 것

1. 직사각형 체크 (0->1)
2. 그래프 전체 순회 -> 0인 애들 bfs로 cnt -> bfs넓이list append
3. sum(넓이list)
"""
import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())

g = [[0] * n for _ in range(m)]
rect = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]


# 직사각형 체크 (0->1)
for xmin, ymin, xmax, ymax in rect:
    for r in range(ymin, ymax):
        for c in range(xmin, xmax):
            if g[r][c] == 1:
                continue
            g[r][c] = 1

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# bfs
def bfs(r, c):
    global g
    cnt = 1

    q = deque([])
    q.append((r, c))

    # 방문했음을 -1의 값으로 표시
    g[r][c] = -1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < m and 0 <= nc < n and g[nr][nc] == 0:
                q.append((nr, nc))
                g[nr][nc] = -1
                
                # 용역넓이
                cnt += 1
    return cnt

cnt = 0
li = []

# 그래프 순회하며 count
for r in range(m):
    for c in range(n):
        if g[r][c] == 0:
            li.append(bfs(r, c))

            # 영역개수
            cnt +=1
li.sort()
print(cnt)
print(' '.join(map(str, li)))
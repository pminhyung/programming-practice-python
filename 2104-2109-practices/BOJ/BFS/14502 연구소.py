"""
1. 벽선택
2. BFS 전염
3. 안전구역 개수 count

# 메모리초과 :
- sys.setrecursionlimit(10 ** 8) 가 메모리를 많이 잡아먹었다!! (재귀깊이가 3이니까 필요x)
- deepcopy도 왠만하면 사용x : 빈배열만들어서 채워라

"""
import sys
#import copy
#sys.setrecursionlimit(10 ** 8)

n, m = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_result = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def spread_virus():
    global max_result
    result = 0

    #cp = copy.deepcopy(g)
    
    # cp = [[0] * m for _ in range(n)]
    # for i in range(n):
    #     for j in range(m):
    #         cp[i][j] = g[i][j]

    cp = [row[:] for row in g]
    
    # virus list 생성 (효율성 UP)
    has_virus = []
    for r in range(n):
        for c in range(m):
            if cp[r][c] == 2:
                has_virus.append((r, c))
    
    # DFS
    while has_virus:
        r, c = has_virus.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and cp[nr][nc] == 0:
                cp[nr][nc] = 2
                has_virus.append((nr, nc))

    for r in range(n):
        for c in range(m):
            if cp[r][c] == 0:
                result += 1
    max_result = max(max_result, result)

# 벽선택
def build_wall(cnt):
    global g
    if cnt == 3:
        spread_virus()
        return

    for r in range(n):
        for c in range(m):
            if g[r][c] == 0:
                g[r][c] = 1
                build_wall(cnt + 1)
                g[r][c] = 0

build_wall(0)
print(max_result)

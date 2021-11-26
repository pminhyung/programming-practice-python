"""
dfs 다소 편하게 구현했지만 시간초과 (dfs가 시간이 더 걸린다)
"""
import sys

R, C = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(R)]
ans = 0

def getnears(r, c, path):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    nears = []
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in path:
            nears.append((nr, nc))
    return nears

def dfs(stack, res, path):
    global ans
    if len(stack)==0:
        ans = max(ans, len(path))
        return

    for r, c in stack:
        nears = getnears(r, c, path + arr[r][c])
        dfs(nears, res + 1, path + arr[r][c])

dfs([(0, 0)], 0, '')
print(ans)
"""
- idea : bfs 활용, t초까지 맵 수정 후 break
- 바이러스 숫자 낮은 순 : sorted(q)
"""
import sys
from collections import deque

def ready_q(arr, n):
    q = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                q.append((arr[i][j], i, j, 0))
    return q

def bfs(arr, n, s):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    q = deque(sorted(ready_q(arr, n)))
    t = 0
    while q:
        v, r, c, t = q.popleft()
        if t==s:
            break
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<=nc<n and arr[nr][nc]==0:
                arr[nr][nc] = v
                q.append((v, nr, nc, t+1))

# main
inp = sys.stdin.readline
n, k = map(int, inp().rstrip().split())
arr = [list(map(int, inp().rstrip().split())) for _ in range(n)]
s, x, y = map(int, inp().rstrip().split())

bfs(arr, n, s)
print(arr[x-1][y-1])
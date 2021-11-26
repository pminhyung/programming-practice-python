"""
정석 -> 시간초과, 왜?

visited의 개념이 따로 없으므로, 배추가 사각형모양일 때는 q에 중복추가 발생
q 이웃추가시 바로 값을 수정한다(방문표시) - 자신과 함께 추가된 이웃을 다시 자신의 이웃으로 추가하지 않음

더불어 처음 bfs시작하는 배추의 경우 먼저 값 수정 후 bfs 시작 (추가되기 전 기준으로 값이 수정되므로)
"""
import sys
from collections import deque

def nears(i, j):
    global arr
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    res = []
    for idx in range(4):
        nr = i + dr[idx]
        nc = j + dc[idx]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
            res.append((nr, nc))
            arr[nr][nc] = 2
    return res


def bfs(i, j):
    global arr
    q = deque([(i, j)])
    while q:
        i, j = q.popleft()
        q += deque(nears(i, j))


t = int(sys.stdin.readline().strip())
for _ in range(t):
    # input
    m, n, k = map(int, sys.stdin.readline().split())

    # arr
    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        j,i = map(int, sys.stdin.readline().split())
        arr[i][j] = 1

    # bfs
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 2
                bfs(i, j)
                cnt += 1


    print(cnt)
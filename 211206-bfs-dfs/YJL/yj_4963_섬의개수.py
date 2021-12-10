import sys
read = sys.stdin.readline
from collections import deque

# 상하좌우 대각선(왼쪽 대각선, 오른쪽 대각선)
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

# bfs로 풀기
def island(i,j):
    queue = deque([(i, j)])
    map_area[i][j] = 0
    # print(queue)
    # deque([(0, 1)])
    # deque([(1, 0)])

    while queue:
        i, j = queue.popleft()
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < h and 0 <= ny < w and map_area[nx][ny] == 1:
                map_area[nx][ny] = 0
                queue.append((nx, ny))    

while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    
    map_area = []
    for _ in range(h):
        map_area.append(list(map(int, read().split())))
    # print('map_area:', map_area)

    count = 0
    for i in range(h):
        for j in range(w):
            if map_area[i][j] == 1:
                island(i, j)
                count += 1
    print(count)


# bfs문제 같음
import sys
input = sys.stdin.readline 
from collections import deque

N, K = map(int, input().split())
test = [] # 전체 맵 정보 담는 리스트
data =[] # 바이러스 정보를 담는 리스트

for i in range(N):
    test.append(list(map(int, input().split())))
    for j in range(N):
        if test[i][j] != 0:
            # 바이러스 숫자, x위치, y위치, 시간 을 입력받는다.
            data.append((test[i][j], i, j, 0))
            # 1 0 0 0 (0,0)
            # 2 0 2 0 (0,2)
            # 3 2 0 0 (2,0)

S, X, Y = map(int, input().split())
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()
q = deque(data)

while q:
    num, x, y, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if test[nx][ny] == 0:
                test[nx][ny] = num
                q.append((num, nx, ny, time+1))

print(test[X-1][Y-1])

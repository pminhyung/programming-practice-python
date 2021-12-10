# 비의 양 조건문을 코드로 만들어내는게 어려워서 답지 참고하면서 풀음
import sys
read = sys.stdin.readline
from collections import deque

N = int(read())
area = []
for _ in range(N):
    area.append(list(map(int, read().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def safeArea(x, y, rain):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
         x, y = queue.popleft()

         for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                 if area[nx][ny] >= rain and visited[nx][ny] == 0:
                     visited[nx][ny] = 1
                     queue.append((nx, ny)) 

# map(function, iterable)
# 1 -> 함수, 2 -> 리스트
rainMin = min(map(min, area))
rainMax = max(map(max, area))

# print(rainMin)  ## 2
# print(rainMax)  ## 9

#  안전한 영역의 최대 개수
rainResult = rainMin
# rainMax+1를 해주는 이유 9가 포함되지 않기 때문 2~8까지만 돈다.
for rain in range(rainMin, rainMax+1):
    visited = [[0] * N for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] >= rain and visited[i][j] == 0:
                safeArea(i, j, rain)
                temp += 1
    if temp > rainResult:
        rainResult = temp
    
print(rainResult)

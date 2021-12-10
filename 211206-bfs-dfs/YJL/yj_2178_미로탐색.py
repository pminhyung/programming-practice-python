# 어떻게 푸는지 감이 안잡혀서 답지 확인 후 코드 이해
# https://velog.io/@norighthere/%EB%B0%B1%EC%A4%80-2178-Python-%EB%AF%B8%EB%A1%9C-%ED%83%90%EC%83%89
# import sys
from collections import deque

N, M = map(int, input().split())
# N, M = map(int, sys.stdin.readline().split())
# # 4 6
# # 101111
# # 101010
# # 101011
# # 111011
miro = []   # 미로

# 미로를 입력
for _ in range(N):
    miro.append(list(map(int, input())))

# 방향을 나타냄
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * M for _ in range(N)]

q = deque([(0, 0)])
# 첫 번째 위치가 문제에 주어져 있으므로 1로 변경
visited[0][0] = 1

while q:
    x, y = q.popleft()

    # 미로의 끝에 도달 했을 때 해당 미로의 값을 호출
    if x == N-1 and y == M-1:
        print(visited[x][y])
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and miro[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
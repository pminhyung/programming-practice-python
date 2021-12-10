import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# n = 7
# graph = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

# 방향을 나타냄
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
# bfs로 풀이
def apartDangi(x, y):
    queue = deque([(x, y)])
    # print('(x,y)', (x,y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                # print('(nx, ny)', (nx, ny))
                queue.append((nx, ny))
                count += 1
        
    return count


result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(apartDangi(i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])

# print(result)

    


import sys
from collections import deque
T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def baechu(field, b,a):
    queue = deque([(b, a)])
    field[b][a] = 0
    # print('(a,b):', (b,a))
    # print('field', field)
    
    while queue:
        b, a = queue.popleft()
        for i in range(4):
            nx = b + dx[i]
            ny = a + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if field[nx][ny] == 1:
                # print('[nx][ny]:', (nx,ny))
                field[nx][ny] = 0
                queue.append((nx, ny))

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * M for _ in range(N)]
    for j in range(K):
        a, b = map(int, sys.stdin.readline().split())
        field[b][a] = 1

    # print(field)
    cnt = 0
    for a in range(M):
        for b in range(N):
            if field[b][a] == 1:
                baechu(field, b,a)
                cnt+=1
    print(cnt)

# 1
# 5 3 6
# 0 2
# 1 2
# 2 2
# 3 2
# 4 2
# 4 0
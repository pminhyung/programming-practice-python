# IndexError: list index out of range때문에 뭐가 문제인지 몰라서 해답봄
# 그 결과 for문 x,y나 i, j를 거꾸로 해야함
import sys
read = sys.stdin.readline
from collections import deque

M, N, K = map(int, read().split())
total_area = [[0] * N for _ in range (M)] 
# print('가로', N, '세로', M)
# print(total_area)
# [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def areaSave(a, b):
    queue = deque([(a, b)])
    total_area[a][b] = 1
    count = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny < M:
                if total_area[ny][nx] == 0:
                    total_area[ny][nx] = 1
                    queue.append((ny, nx)) 
                    count += 1
    return count
    

for _ in range(K):
    xl, yl, xr, yr = map(int, read().split())
    
    # width_max = max([left_x, right_x])
    # width_min = min([left_x, right_x])
    # height_max = max([left_y, right_y])
    # height_min = min([left_y, right_y])

    for h in range(yl, yr):
        for w in range(xl, xr):
                total_area[h][w] = 1

result = []
for m in range(M): # 세로
    for n in range(N): # 가로
        if total_area[m][n] == 0:
            total_area[m][n] = 1
            result.append(areaSave(m, n))

print(len(result))
result.sort()
for num in result:
    print(num,end=" ") 
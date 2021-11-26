"""
# 문제 잘읽자

- 조건: 아무지역도 안잠길 수 있다 (0<k<max_k)

# visited 배열을 똑같이 만들어서 check
# 주변미탐색지역을 queue 또는 stack에 넣을 때 함수 정의(add_near)
# dfs stack에 지역추가할때도, 배열 순회할 때도 모두 visited에 있는지 check
"""

import sys
sys.setrecursionlimit(10**8)

#dfs
def add_near(x,y):
    global visited

    news = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if arr[ny][nx] > k and (not visited[ny][nx]):
                news.append([nx, ny])

    return news

def dfs(x,y):
    stack = [[x,y]]
    while stack:
        x,y = stack.pop()
        visited[y][x] = True
        stack += add_near(x,y) # 주변미탐색지역들 put

#inp
n = int(sys.stdin.readline().strip())

#arr
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#k range
max_k = max([max(arr[i]) for i in range(n)])

#search
max_safe = 0
#for k in range(min_, max_+1):
for k in range(0, max_k+1): # 조건: 아무지역도 안잠길 수 있다
    visited = [[False] * n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]>k and (not visited[i][j]): ##### dfs를 시행할 노드도 visited check!!!
                dfs(j,i) # x,y
                cnt+=1

    if max_safe<cnt:
        max_safe=cnt

print(max_safe)
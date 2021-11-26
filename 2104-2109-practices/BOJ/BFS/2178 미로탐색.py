"""
bfs로 주변 노드를 추가할 때 이전노드까지의 거리비용+1을 대입해준다
방문한 노드들은 1보다 값이 크므로, 1인 애들만 추가되도록 하면 visited를 사용하지 않아도 된다.
"""
import sys
sys.setrecursionlimit(10**8)


n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

from collections import deque

q = deque([(0,0)])
visited = []
cnt = 0

# while (m-1, n-1) not in visited:
while q:
    x,y = q.popleft()
    # if (x,y) not in visited:
    for i in range(4): # 방향
        new_x = x+dx[i]
        new_y = y+dy[i]
        if (0<=new_x<=m-1) and (0<=new_y<=n-1):
            if (arr[new_y][new_x]==1):
                arr[new_y][new_x] = arr[y][x]+1
                q+=[(new_x,new_y)]
    # visited.append((x,y))

print(arr[n-1][m-1])
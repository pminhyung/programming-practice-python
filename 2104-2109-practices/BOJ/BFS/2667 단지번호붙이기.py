"""
논리는 잘세웠다

초깃값(1)보다 높은 2부터 라벨을 줌으로써 visited 기능 수행

## 항상 pop한 node가 기준!!! (line 30-32)
- 초깃값 또한 라벨을 붙여줘야함
- 집단 개수 cnt+1은 popleft를 하는 시점부터 해줄 것

q에 추가할 때는 초깃값인지와, 이미 다른 노드의 이웃으로서 q에 추가되었는지 확인한다 (line 40)
- pop할 때만 visited처리(라벨할당)가 이루어지기 때문이다!
"""
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
cnt = 1
dcnts = []

dx=[1,-1,0,0]
dy=[0,0,1,-1]

# bfs
def bfs(x,y):
    global dcnts
    q=deque([[x,y]])
    dcnt=0

    while q:
        x,y = q.popleft()
        dcnt += 1
        arr[y][x] = cnt

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<=n-1) and (0<=ny<=n-1):
                if (arr[ny][nx]==1) and ([nx,ny] not in q):
                    q+=[[nx,ny]]

    dcnts.append(dcnt)

for y in range(n):        # x
    for x in range(n):    # y
        if arr[y][x]==1:
            cnt+=1
            bfs(x,y)

print(str(len(dcnts))+'\n'+'\n'.join(map(str,sorted(dcnts))))
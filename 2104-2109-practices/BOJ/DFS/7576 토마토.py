"""
쉽게생각했어도 되는문제..

-1, 0이 되는 우선순위 및 조건을 따지고 완전탐색으로 예외처리해도 됨...
"""
import sys
from collections import deque
m,n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def get_near(r,c):
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    near = []
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        near.append((nr,nc))
    return near # list

def bfs():
    global arr
    q = deque(tom.copy())
    maxim=1

    while q:
        r,c = q.popleft()
        near = get_near(r,c)
        for nr,nc in near:
            if 0<=nr<n and 0<=nc<m and arr[nr][nc]==0:
                arr[nr][nc]=arr[r][c]+1
                q+=deque([(nr,nc)])
                maxim = max(maxim, arr[nr][nc])
        #print(arr)
    return maxim

# 원본 0체크, 없으면 0 출력
tom = []
zero_cnt=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            zero_cnt+=1
            continue

        if arr[i][j]==1:
            tom.append((i,j))
def main():
    if zero_cnt==0:
        print(0)
        return

    # bfs (시작점 하루 제외)
    ans = bfs()-1

    # bfs이후 0체크, 있으면 -1 출력
    left=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                left+=1

    if left!=0:
        print(-1)
        return
    print(ans)

main()

"""
백트래킹시 bfs를 사용하면 시간을 줄이면서 같은 함수레벨에서 돌 수 있다
step에 추가하며 계속 q에 넣어준다
max(ans, len(step))도 꿀팁
"""
import sys
R,C = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(R)]
ans=0

def bfs():
    global ans
    q = set()
    q.add((0, 0, arr[0][0]))
    while q:
        r,c,step = q.pop()
        ans = max(ans, len(step))
        dr=[0,0,1,-1]
        dc=[1,-1,0,0]
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<R and 0<=nc<C and arr[nr][nc] not in step:
                q.add((nr,nc,step+arr[nr][nc]))
bfs()
print(ans)
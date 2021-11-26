"""
재귀 숙련에 따른 난이도 체감

- 후진시 후진방향과 원래방향 구별해야
- 벽과 방문여부는 동일한 그래프에서 1,2의 값으로 표현가능
"""
import sys
sys.setrecursionlimit(10**8)

def clean(r,c,d):
    global ans

    # 청소
    if g[r][c]==0:
        g[r][c]=2
        ans+=1

    # 회전
    for _ in range(4):
        d = (d+3)%4
        nr = r+dr[d]
        nc = c+dc[d]
        if g[nr][nc]==0:
            return clean(nr,nc,d)
    # 후진
    nd = (d+2)%4 # 후진방향과 원래방향 구별
    nr = r+dr[nd]
    nc = c+dc[nd]

    if g[nr][nc]==1:
        return
    else:
        clean(nr, nc, d)

n, m = map(int, sys.stdin.readline().split())
cr, cc, d = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]
ans = 0

clean(cr, cc, d)
print(ans)
"""
DFS, 백트래킹
시간초과 -> 백트래킹 필요
"""
import sys
sys.setrecursionlimit(10**8)

#add_near
def add_near(x, y):
    news=[]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<c) and (0<=ny<r) and (arr[ny][nx] not in prevs):
            news.append([nx,ny])
    return news

#dfs
def dfs(x,y):
    global prevs, max_cnt
    stack =[[x,y]]
    cnt=0
    while stack:
        x,y = stack.pop()
        if arr[y][x] not in prevs:
            prevs.append(arr[y][x])
            cnt+=1
            news=add_near(x,y)
            if len(news)==0:
                if max_cnt<cnt:
                    max_cnt=cnt
                cnt, prevs=1, [prevs[0]]
            stack += news
#input
r,c = map(int, sys.stdin.readline().split())

#graph
arr= [sys.stdin.readline().strip() for _ in range(r)]

#traverse
prevs= []
max_cnt, cnt = 0, 0

dfs(0,0)
print(max_cnt)
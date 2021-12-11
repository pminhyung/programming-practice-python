"""
- 상하대칭으로 생각한다면 convert가 필요없는 문제 
- (y2가 실제 column범위를 벗어나지만 range함수 사용으로 +1 필요없이 넣을 수 있다)
"""
import sys

def dfs(r,c):
    stack = [(r,c)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    area = 0
    while stack:
        r,c = stack.pop()
        area+=1
        g[r][c]=1 # visited
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<m and 0<=nc<n and g[nr][nc]==0 and (nr,nc) not in stack:
                stack.append((nr, nc))
    return area

inp = sys.stdin.readline
m, n, k = map(int, inp().rstrip().split())

# 직사각형 영역 1로 표시
rects = [list(map(int, inp().rstrip().split())) for _ in range(k)]
g = [[0 for _ in range(n)] for _ in range(m)]
for x1, y1, x2, y2 in rects:
    for i in range(y2, y1):
        for j in range(x1, x2):
            g[i][j] = 1 

# 영역개수 count (dfs)
cnt = 0
areas = []
for i in range(m):
    for j in range(n):
        if g[i][j]==0:
            area = dfs(i,j) # dfs : 영역넓이
            cnt+=1
            areas.append(area)
    
print(f"{cnt}\n{' '.join(map(str,sorted(areas)))}")
"""
문제 잘 읽자 (input - 배열과 좌표의 가로세로 개수 및 좌표 입력순서)

bfs : queue 초깃값 넣고 while queue -> for방향이동: queue pop(), 조건:append
"""
def bfs(x,y):
    q = [[x,y]]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        curr_x, curr_y = q.pop()
        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            if (0<=next_x<N) and (0<=next_y<M) and (arr[next_x][next_y]==1):
                q.append([next_x, next_y])
                arr[next_x][next_y] = 0

T = int(input())

for t in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        arr[y][x] = 1
    for i in range(N):
        for j in range(M):
            if (arr[i][j] ==1):
                bfs(i,j)
                arr[i][j]=0
                cnt+=1
    print(cnt)

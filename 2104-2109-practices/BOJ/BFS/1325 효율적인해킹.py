"""
시간 초과 미쳤다....

0. pypy3가 핵심... (없었으면 불가능)
1. import sys; input = sys.stdin.readline (input속도를 빠르게 한다)
2. list대신 deque 사용 (queue로 사용할 땐 빠르다, append와 popleft())
3. 마지막에 cnt최댓값에 해당하는 pc번호: cnt최댓값일 때는 result초기화 후 pc번호 넣어줌, 기존최댓값과 같을 때는 result에 append
4. DP(N+1 만들고 True, False 맵핑) arr(2차배열 그래프) 사용할 것


"""
import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())

def bfs(k):
    q = deque()
    q.append(k)
    cnt=0
    visited = [False] * (N+1)
    visited[k] =True
    while q:
        k = q.popleft()
        cnt += 1
        for n in arr[k]:
            if not visited[n]:
                q.append(n)
                visited[n] = True
    return cnt

# 그래프 생성
arr = [[]*M for _ in range(N+1)] # index 0은 무시
for _ in range(M):
    x,y = list(map(int, input().split())) # [x,y]
    arr[y].append(x)

nodes = []
max= 0
for k in range(1, N+1):
    if arr[k]:
        cnt = bfs(k)
        if cnt>=max:
            if cnt>max:
                nodes=[]
            max = cnt
            nodes.append(k)
print(*nodes)
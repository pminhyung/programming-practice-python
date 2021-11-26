"""
(진행중)
우선순위큐와 BFS 활용

while t<=K:
1-1. 활성화 -> 비활성화 (번식)
1-2. 활성화 -> 죽음
2. 비활성화 -> 활성화
"""


# input
T = int(input()) # T 테스트개수

for test_case in range(1, T+1):
    N, M, K = map(int, input().split()) # 행, 열, 종료시간

    # board 생성
    maximum = 350 # board 최대 크기 (350x350 - 댓글참고) ---- 근데 왜 350일까.....
    t = 0         # 현재시간
    board = [[] for i in range(maximum)]
    roots = [] # 시작좌표들 - 0이 아닌 (x,y)

    for i in range(maximum//2, maximum+1):
        li = list(map(int, input().split()))
        board[i] = li
        roots.extend([(i,j) for j in range(len(li)) if li[j]!=0])

    vital = {(i,j):board[i][j] for i,j in roots} # {좌표:생명력지수}

    res = bfs(roots)
    print('#{} {}'.format(test_case, res))

#from queue import PriorityQueue
import heapq
def bfs(roots):
    global t, K
    d=[(0, -1), (0,1), (1,0), (-1,0)]
    active, nonactive = [], []
    dead = []

    for x, y in roots:
        #nonactive.put((vital[(x, y)], (x, y)))  # (생명력지수, (x,y))
        heapq.heappush(nonactive, (vital[(x, y)], (x, y))) # (생명력지수, (x,y))
    t+=1

    num_active = [0] * (t+1)
    while t<=K:
        # 1-1. 활성화 -> 비활성화(번식)
        if len(active)!=0:
            heapq.heappop(active, )

            for
        # 1-2. 활성화 -> 죽음

        # 2. 비활성화 -> 활성화














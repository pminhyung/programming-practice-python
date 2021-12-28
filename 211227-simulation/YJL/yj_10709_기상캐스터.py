# 문제 출력 부분 이해 안됨
# https://ywtechit.tistory.com/218

import sys
input = sys.stdin.readline 

H, W = map(int, input().split())
sky = [list(input().rstrip()) for _ in range(H)]
answer = [[0] * W for _ in range(H)]

for i in range(H):
    # 각 row를 기준으로 cnt와 cloud를 초기화 시킨다.
    cnt = 1
    cloud = False
    for j in range(W):
        # 현재 좌표가 .인데 not cloud면 -1을 넣는다. (이전까지 구름이 없으므로)
        if not cloud and sky[i][j] == '.':
            answer[i][j] = -1
        # 현재 좌표가 c면 0을 넣는다. (구름이 현재 떠있는 상태이므로)
        elif sky[i][j] == 'c':
            cloud = True
            answer[i][j] = 0
            cnt = 1
        # 현재 좌표가 .인데 cloud면 이전까지 누적한 cnt를 넣는다. (구름이 cnt분 뒤에 오기 때문에)
        elif cloud and sky[i][j] == '.':
            answer[i][j] = cnt
            cnt += 1

for i in answer:
    print(*i, end=' ')
    print()
"""
- 원형큐 사용 (힙큐와 우선순위 큐 사용 시도 -> 조건이 원형큐에 적합)
"""
import sys
from collections import deque

inp = sys.stdin.readline
ntest = int(inp().rstrip())

def get_print_cnt(n, m, priors):
    idx = deque(list(range(n)))
    cnt = 0
    while True:
        # 인쇄
        if priors[0] == max(priors):
            priors.popleft()
            curr = idx.popleft()
            cnt+=1

            # 종료
            if curr==m:
                break

        # 후순위 이동
        else:
            priors.append(priors.popleft())
            idx.append(idx.popleft())
    return cnt

for _ in range(ntest):
    n, m  = map(int, inp().rstrip().split())
    priors = deque(list(map(int, inp().rstrip().split())))
    print(get_print_cnt(n, m, priors))
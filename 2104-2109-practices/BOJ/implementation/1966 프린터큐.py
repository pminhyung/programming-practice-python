"""
동일한 순서간에도 구별 가능하도록 고유한 index(enumerate 또는 boolean) 사용!

"""

import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = map(int,sys.stdin.readline().split())
    q = deque(list(map(int,sys.stdin.readline().split())))
    idq = deque([0]*len(q))
    idq[m]=1
    res=0

    while True:
        if max(q)>q[0]:
            q.append(q.popleft())
            idq.append(idq.popleft())
            continue
        if idq[0]==1:
            res+=1
            print(res)
            break
        q.popleft()
        idq.popleft()
        res+=1
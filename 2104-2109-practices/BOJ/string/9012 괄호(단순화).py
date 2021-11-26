"""
배열원소를 하나씩 pop하며 특정괄호cnt 증감
0일때만 YES (개수 같음), 혹은 NO
"""
import sys
sys.setrecursionlimit(10**8)
from collections import deque

T = int(sys.stdin.readline().strip())

for _ in range(T):
    arr = deque(map(str, sys.stdin.readline().strip()))
    left_cnt=0
    while len(arr)!=0:

        if left_cnt<0:
            break

        curr = arr.popleft()

        if curr =='(':
            left_cnt+=1
        else:
            left_cnt-=1

    if left_cnt==0:
        print('YES')
        continue
    print('NO')
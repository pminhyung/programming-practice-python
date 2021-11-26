"""
DP로 풀어야...
"""

import sys
n = int(sys.stdin.readline())
st = ''.join(sys.stdin.readline().split())
nq = int(sys.stdin.readline())

def comp(s,e):
    temp = st[s-1:e]
    l =len(temp)
    for i in range(l//2):
        if temp[i]!=temp[l-1-i]:
            return False
    return True

for _ in range(nq):
    s, e = map(int, sys.stdin.readline().split())
    if s==e:
        print(1)
        continue
    if comp(s,e):
        print(1)
        continue
    print(0)
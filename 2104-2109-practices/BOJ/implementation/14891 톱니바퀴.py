import sys
from collections import deque

w = {}
for i in range(1,4+1):
    w[i] = deque(list(map(int, sys.stdin.readline().strip().strip())))

def is_rot(n:int, n2:int):
    if n>n2:
        if w[n][2]!=w[n2][6]:
            return True
    if w[n][6]!=w[n2][2]:
        return True
    return False


def rot_near(n, nears:list):
    global dr
    for ne in nears:
        if is_rot(n, ne):
            dr = -dr
            rot(ne, dr)
            continue

def rot(n,dr):
    if dr==0:
        return
    if dr==1:
        last = w[n].pop()
        w[n] = deque([last]) + w[n]
    elif dr==-1:
        last = w[n].popleft()
        w[n].append(last)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, dr = map(int,sys.stdin.readline().split())
    if n==1:
        rot(n,dr)
        rot_near(n,[n+1])
    elif n==4:
        rot(n,dr)
        rot_near(n,[n-1])
    else: # 2,3
        rot(n,dr)
        rot_near(n, [n+1, n-1])

sum = 0
for k in w:
    twelve = w[k][0]
    if twelve: # S극
        sum+=2**(k-1)

print(sum)

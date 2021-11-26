"""
sys.stdin.readline()은 '\n'을 포함하므로 split 안쓸 땐 꼭 strip() 써야한다
reverse와 pop의 index 규칙을 실제 역전 없이 로직구현해야. pop(0 또는 -1)이 되도록

아직 시간초과....
"""
import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for t in range(T):
    comm = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    arr = sys.stdin.readline().strip()

    #print(comm, n, arr)
    if (n < comm.count('D')) or (arr=='[]'):
        print('error')
        continue

    arr = arr.replace('[', '').replace(']', '').split(',')
    arr = list(map(int, arr))

    comm = comm.replace('RR', '')
    dir, l, r = 1, 0, 0
    for c in comm:
        if c=='R':
            dir= not dir # arr=queue(list(reversed(arr)))
        elif c=='D':
            if dir:
                l+=1
            else:
                r+=1
    if r==0:
        arr = arr[l:]
    else:
        arr = arr[l:-r]

    if len(arr)==0:
        print('[]')
        continue

    if not dir:
        print('['+','.join(map(str,reversed(arr)))+']')
    else:
        print('[' + ','.join(map(str, arr)) + ']')
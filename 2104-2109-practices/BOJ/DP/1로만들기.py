"""
배열길이 미리 정하지 않고, arr.append

n//3, n//2 존재 하지 않을때는?
-> math.inf 이용하거나, iter마다 temp=[] 두고 해당될때만 append해서 마지막에 min 비교

bfs로 풀수도 있다
https://blockdmask.tistory.com/257?category=250801
"""
import sys
import math
n = int(sys.stdin.readline().strip())
arr = [0,0,1,1]
if n<=3:
    print(arr[n])
else:
    for i in range(4, n+1):
        a,b,c = math.inf, math.inf, arr[i-1]+1
        if not i%3:
            a = arr[i//3]+1
        if not i%2:
            b = arr[i//2]+1
        arr.append(min(a,b,c))
    print(arr[n])
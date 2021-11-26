"""
서로 다른 카드를 쓰므로 중첩시 i+1, j+1부터
"""
import sys
n,m = map(int,sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

res=0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_ = li[i]+li[j]+li[k]
            if sum_<=m:
                res = max(res, sum_)
print(res)
"""
자신보다 낮은 수들에 대해 증가하는수열 길이+1만 하는 것이 핵심이다

10 20 30 50 20 이면
1 2 3 4 4 가 아닌
1 2 3 4 2 가 되어야 맞다 (자신과 앞에있는 자신보다 낮은 숫자들만 카운트해야.)

예시)
10 20 30 50 21 31 32 33 34

1) 1 2 3 4 4 4 4 4 4 -> 4
2) 1 2 3 4 2 3 4 5 6 -> 6
"""
import sys
n=int(sys.stdin.readline().strip())
arr=[0]+list(map(int,sys.stdin.readline().split()))
dp=[0]+[1]*n

for i in range(2, n+1):
    for j in range(1, i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[j]+1, dp[i])
print(max(dp))
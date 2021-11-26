"""
곡바뀌는 것을 행으로, 볼륨 범위를 열로하여 각 곡마다 볼륨 후보에 True를 기록하는 방식.

출력시 result 변수에 따로 담고 출력하는 습관들이자... (바로 for문에서 출력 시 왜 틀리는지는 모르곘다 ㅠ)
if조건문에서 새로운 변수할당 시에는 전역변수로 미리 할당해야 (런타임에러 nameerror 방지)
"""

import sys
n,s,m=map(int, sys.stdin.readline().split())
array = [0]+list(map(int, sys.stdin.readline().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s]=1

for i in range(1,n+1):
    for j in range(m+1):
        # 이전(i-1) 볼륨값 True(j) 찾기
        if dp[i-1][j]==0:
            continue

        # 새로운 볼륨 후보 True
        if j-array[i]>=0:
            dp[i][j-array[i]]=1
        if j+array[i]<=m:
            dp[i][j+array[i]]=1

# 볼륨 최댓값 출력
res=-1
for j in range(m,-1,-1):
    if dp[n][j]==1:
        res=j
        break
print(res)
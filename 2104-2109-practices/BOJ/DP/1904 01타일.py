"""
문제 입력,출력부분도 잘읽어라... 15,746으로 나눈 나머지를 출력..

마지막만 나누는 것이 아니라 각 단계에서 계산 시 계속 나눈다:
(A+B)%C = (A%C + B%C)%C 모듈러의 법칙
"""
import sys
n = int(sys.stdin.readline())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])


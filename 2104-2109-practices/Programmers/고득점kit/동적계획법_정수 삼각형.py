"""
참고: https://codedrive.tistory.com/49

양끝은 윗줄 양끝의 합을 그대로 더해준다
가운데 부분에서 윗줄 결과 두개중 큰것만 더하면, DP가 그대로 피라미드 형태가 유지된다
"""

def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    t = triangle

    for i in range(len(triangle)):
        if i == 0:
            dp[i] = [t[0][0]]
            continue
        for j in range(i + 1):
            if j == 0:
                dp[i].append(dp[i - 1][j] + t[i][j])
                continue
            if j == i:
                dp[i].append(dp[i - 1][j - 1] + t[i][j])
                continue
            dp[i].append(max(dp[i - 1][j - 1], dp[i - 1][j]) + t[i][j])
    return max(dp[-1])
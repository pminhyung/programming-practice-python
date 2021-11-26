"""
완전한 순위계산이 가능한 노드:

i에게 진 선수는 i가 진 선수들에게 진다
i를 이긴 선수는 i가 이긴 선수들도 이긴다

i가 이기고 지는 선수 기록이 n-1명이면 완전한 순위계산 가능
"""

def solution(n, results):
    ans = 0
    win = [False] + [set() for _ in range(n)] # i가 이긴 선수
    lose = [False] + [set() for _ in range(n)] # i를 이긴 선수

    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)

    for i in range(1, n + 1):
        # i에게 진 선수는 i가 진 선수들에게 진다
        for loser in win[i]:
            lose[loser].update(lose[i])

        # i를 이긴 선수는 i가 이긴 선수들도 이긴다
        for winner in lose[i]:
            win[winner].update(win[i])

    for i in range(1, n + 1):
        # i가 이기고 지는 선수 기록이 n-1명이면 완전한 순위계산 가능
        if len(win[i]) + len(lose[i]) == n - 1:
            ans += 1

    return ans
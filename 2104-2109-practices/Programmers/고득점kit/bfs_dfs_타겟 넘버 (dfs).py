"""
일반 dfs, 재귀 dfs 구현

프로그래머스에서는 함수기반이기 때문에 내부함수 정의시 전역변수 2번 정의!
"""
def solution(numbers, target):
    # dfs
    from collections import deque
    ans = 0
    last = len(numbers) - 1
    q = [(-1, 0)] # ind, tot

    while q:
        ind, tot = q.pop() # stack 사용 차이
        if ind == last:
            if tot == target:
                ans += 1
            continue
        q.append((ind + 1, tot + numbers[ind + 1]))
        q.append((ind + 1, tot - numbers[ind + 1]))
    return ans

# 재귀 dfs
def solution(numbers, target):
    # dfs
    global ans
    ans = 0
    last = len(numbers) - 1

    def dfs(ind, tot):
        global ans
        if ind == last:
            if tot == target:
                ans += 1
            return
        dfs(ind + 1, tot + numbers[ind + 1])
        dfs(ind + 1, tot - numbers[ind + 1])

    dfs(-1, 0)
    return ans


print(solution([1, 1, 1, 1, 1], 3))

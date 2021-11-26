"""
계산값 자체를 node로 graph화 -> bfs 가능!
"""
def solution(numbers, target):
    # bfs
    from collections import deque
    ans = 0
    last = len(numbers) - 1
    q = deque()
    q.append((-1, 0)) # ind, tot

    while q:
        ind, tot = q.popleft() # queue 사용 차이
        if ind == last:
            if tot == target:
                ans += 1
            continue
        q.append((ind + 1, tot + numbers[ind + 1]))
        q.append((ind + 1, tot - numbers[ind + 1]))
    return ans
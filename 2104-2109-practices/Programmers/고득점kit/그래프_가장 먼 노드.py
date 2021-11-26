"""
visited를 "node not in v" 사용보다 "v[node] = False, True" 로 사용해야 효율성 통과!
"""
def solution(n, edge):
    g = [False] + [[] for _ in range(n)]

    # graph
    for src, tg in edge:
        g[src].append(tg)
        g[tg].append(src)

    # bfs
    from collections import deque

    q = deque([])
    q.append((1, 1))  # node, dist
    v = [False] + [True] + [False] * (n - 1) # 1번 node 방문처리
    longest = 0
    cnt = 0
    
    while q:
        curr, dist = q.popleft()
        if longest < dist:
            longest = dist
            cnt = 1
        else:
            cnt += 1

        for node in g[curr]:
            if not v[node]:
                q.append((node, dist + 1))
                v[node] = True

    return cnt
def solution(n, computers):
    # bfs 함수정의
    def bfs(i):
        from collections import deque
        q = deque()
        q += deque(arr[i])
        v = []
        while q:
            curr = q.popleft()
            if curr not in v:
                q += deque(arr[curr])
                v.append(curr)
        return v
    
    # graph 정의
    arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                arr[i].append(j)
    
    # bfs실행
    ans = 0
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        if len(visited) == n:
            break
        visited.update(bfs(i))
        ans += 1
    return ans
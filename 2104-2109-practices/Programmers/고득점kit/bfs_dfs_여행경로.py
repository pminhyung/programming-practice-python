"""
미리 sort를 사용 ->  경로 완성 시 바로 return하면 정답

deepcopy와 재귀를 사용함으로써 경로완성이 안된 경우 back이 가능 ->  paths 개수가 N+1이면 완료

enumerate와 list.insert, defaultdict를 통해 pop을 다시 원상복구 가능하다!
"""

def solution(tickets):

    from collections import defaultdict

    N = len(tickets)

    def dfs(graph, paths, start):

        if len(paths) == N + 1:
            return paths

        for idx, target in enumerate(graph[start]):
            graph[start].pop(idx)
            tmp = paths[:] # deepcopy
            tmp.append(target)

            ans = dfs(graph, tmp, target)

            if ans:
                return ans
            
            # 정답완성이 안됐다면 pop 행위를 다시 복구
            graph[start].insert(idx, target)

    g = defaultdict(list)
    for t in tickets:
        g[t[0]].append(t[1])
        g[t[0]].sort()

    answer = dfs(g, ['ICN'], 'ICN')  # graph(dict), paths(list), start(str)
    return answer
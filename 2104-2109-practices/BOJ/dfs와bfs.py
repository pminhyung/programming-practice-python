# 그래프 입력 및 생성
n_node, n_edge, root = map(int, input().split())

graph = {}
for _ in range(n_edge):
    n1,n2 = list(map(int,input().split()))
    pair = [n1,n2]

    for i in range(2): # 받은 pair 모두 각각 k, v로 입력
        if pair[i] in graph:
            graph[pair[i]].append(pair[1-i])
        else:
            graph[pair[i]] = [pair[1-i]]

#print(graph)

def dfs(graph, root):
    need_visit, visited = [], []
    need_visit.append(root)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return ' '.join(map(str,visited))

def bfs(graph, root):
    need_visit, visited= [], []
    need_visit.append(root)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return ' '.join(map(str, visited))

# node가 한개일 때 root출력
if n_node <= 1:
    print(root)
    print(root)
else:
    # stack(LIFO)니까 연결노드들 내림차순
    res_dfs = dfs({k:sorted(v, reverse=True) for k,v in graph.items()}, root)

    # queue(FIFO)니까 연결노드들 오름차순
    res_bfs = bfs({k:sorted(v) for k,v in graph.items()}, root)

    print(res_dfs)
    print(res_bfs)
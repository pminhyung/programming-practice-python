# O(V+E)
graph = {
    'A':['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'G', 'H', 'I'],
    'D':['B', 'E', 'F'],
    'E':['D'],
    'F':['D'],
    'G':['C'],
    'H':['C'],
    'I':['C','J'],
    'J':['I']
}

def bfs(graph, root):
    need_visit, visited = [], []
    
    # root 먼저 append
    need_visit.append(root)
    
    # need_visit에서 pop(0)
    # visited에 없으면 추가 및 need_visit에 자식노드 추가
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            need_visit.extend(graph[node])
            visited.append(node)
    return visited

print(bfs(graph, 'A'))

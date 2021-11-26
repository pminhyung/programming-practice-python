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

def dfs(graph, root):
    need_visit, visited= [], []
    need_visit.append(root)
    while need_visit:
        # stack 사용 (LIFO, 오른쪽 node를 마지막에 graph에서 위치시키니까 오른쪽부터 순회)
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

print(dfs(graph, 'A'))
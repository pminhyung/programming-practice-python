[list][copy][graph 복사][bfs][dfs]
- 함수 내부에서 list 객체 내용 수정 시, 전역적으로도 해당 객체가 수정된다 (복사되지 않음)
- 1차원 리스트 깊은 복사는 list[:], []+list, list.copy() 로 가능하나, 2차원 이상은 deepcopy를 사용해야 깊은복사 가능
- 그러나 deepcopy는 시간이 매우 오래걸리므로 코테에서는 시간초과 발생
- 특히 bfs, dfs에서 graph를 계속 수정해야 한다면 graph를 deepcopy하는 대신, visited 배열을 만들어서 사용하고 bfs 및 dfs 내 append 조건문에도 not in q(stack) 대신, not visited[nr][nc] 로 대체할 것

- 단순 graph 생성 시 defaultdict(list) 이용할 것 (정수 key 사용 가능) ex. graph = defaultdict(list)

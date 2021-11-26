"""
zip 함수로 철자 다른 것 count -> 1인 단어 출력
generator를 사용!
"""
def solution(begin, target, words):
    from collections import deque

    def get_next(curr, words):
        for word in words:
            cost = 0
            for w1, w2 in zip(curr, word):
                if w1 != w2:
                    cost += 1
            if cost == 1:
                yield word

    def bfs(begin):
        dist = dict()
        dist[begin] = 0
        q = deque()
        q.append(begin)

        while q:
            curr = q.popleft()
            for nex in get_next(curr, words):
                if nex not in dist:
                    dist[nex] = dist[curr] + 1
                    q.append(nex)
        return dist

    return bfs(begin).get(target, 0)
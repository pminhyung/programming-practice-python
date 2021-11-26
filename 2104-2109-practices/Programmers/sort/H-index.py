def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

# [50, 40, 30, 11, 8, 4, 2] -> 5
# [3, 0, 6, 1, 5] -> 3

def solution(citations):
    citations.sort(reverse=True)
    h = map(min, enumerate(citations, start=1)) # ind는 더 큰 원소개수
    return max(h)
# collections 이용(값:횟수), 객체끼리 뺄셈 가능
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# hash로 정수값을 더하여 container로 사용, 뺄셈으로 차집합 수행, 남은hash값의 value 반환
def solution(participants, completion):
    d = {hash(p): p for p in participants}

    temp = sum([hash(p) for p in participants])
    temp = temp - sum([hash(c) for c in completion])

    return d[temp]

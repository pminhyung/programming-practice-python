"""
문제잘읽자: 여벌가진 학생이 잃어버리는 경우도 존재
"""
def solution(n, lost, reserve):
    lost_t = set(lost) - set(reserve)
    reserve_t = set(reserve) - set(lost)

    for i in reserve_t:
        if i - 1 in lost_t:
            lost_t.remove(i - 1)
        elif i + 1 in lost_t:
            lost_t.remove(i + 1)
    return n - len(lost_t)
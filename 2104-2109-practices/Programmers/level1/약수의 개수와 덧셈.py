"""
제곱수이면 약수개수가 홀수개
"""
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if int(n**.5)==n**.5:
            answer-=n
        else:
            answer+=n
    return answer


def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        li = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                li.append(i)
        if len(li) % 2:
            answer += n
        else:
            answer -= n

    return answer
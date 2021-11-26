# 에라토스테네스의 체 : 제곱근까지의 소수 배수들을 모두 제거하고 남는 수들은 소수들
def solution(n):
    sqrt = int(n ** .5)
    arr = ['_', False] + [True] * (n - 1)
    for i in range(2, sqrt + 1):
        for j in range(i * 2, n + 1, i):
            if arr[i] == True:
                arr[j] = False
    return sum(arr[2:])


def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
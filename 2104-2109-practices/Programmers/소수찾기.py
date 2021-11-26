from itertools import permutations

def solution(numbers):
    li = []
    for i in range(1, len(numbers)+1):
        li+=permutations(numbers, i)

    comb = list(set([int(''.join(list(pair))) for pair in li]))

    sosu = []

    def is_prime(n):
        sqrt = int(n**.5)
        if (n == 0) or (n == 1):
            return False
        for s in range(2, sqrt+1):
            if n%s==0:
                return False
        return True

    for n in comb:
        if is_prime(n):
            sosu.append(n)
    return len(set(sosu))




    # for n in comb:
    #     sqrt = int(n**.5)
    #     arr = [False]+[True]*(n-1) # 10
    #     for i in range(2, sqrt+1): # 2, 3
    #         if arr[i-1] == True:
    #             arr[i-1] = False
    #             for j in range(i*2, n+1, i):
    #                 arr[j-1] = False
    #                 print(arr)
    #                 break
    #     if sum(arr)==2:
    #         sosu.append(n)
    # return len(sosu)

print(solution('011'))


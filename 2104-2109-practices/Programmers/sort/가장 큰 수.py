## 시간초과
# from itertools import permutations
# def solution(numbers):
#     comb = permutations(list(map(str,numbers)), len(numbers))
#     return str(max([int(''.join(c)) for c in comb]))

###
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) # input이 1,000 이하이므로 세자리 만들어서 비교, 문자열 정렬 시 인덱스별로 ascii코드 비교
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))
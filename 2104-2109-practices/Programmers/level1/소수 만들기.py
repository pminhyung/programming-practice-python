from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])


from itertools import combinations
def solution(nums):
    ns = [sum(i) for i in combinations(nums, 3)]
    sosu = []
    for n in ns:
        is_sosu=True
        for i in range(2, int(n**.5)+1):
            if n%i==0:
                is_sosu=False
                break
        if is_sosu:
            sosu.append(n)
    return len(sosu)
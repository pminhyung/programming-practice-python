def solution(numbers):
    # card list 생성 (split)
    cards = [i for i in numbers]

    # card 조합 permutations
    from itertools import permutations
    combs = []
    for i in range(1, len(cards)+1):
        combs += permutations(cards, i)

    # card 조합된 숫자 순회, check_prime
    comb_nums = list(set([int(''.join(c)) for c in combs]))
    sosu = []

    def check_prime(n):
        if (n==0) or (n==1):
            return False
        sqrt= int(n**.5)
        for i in range(2, sqrt+1):
            if n%i==0:
                return False
        return True

    for n in comb_nums:
        if check_prime(n):
            sosu.append(n)

    # 개수 return
    return len(set(sosu))

print(solution('011'))


def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer))) # sort 주의
    return answer


from itertools import combinations
def solution(numbers):
    answers = set()
    for comb in combinations(numbers, 2):
        answers.add(sum(comb))
    return sorted(list(answers))


def solution(numbers):
    return sorted(list(set(sum(comb) for comb in combinations(numbers, 2))))


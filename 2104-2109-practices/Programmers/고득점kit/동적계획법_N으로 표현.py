"""
참고: https://gurumee92.tistory.com/164

초반에 N값을 예제값으로 넣지말 것! (line 18)

"""

def solution(N, number):
    # 예외처리 (number이 0, N일 때)
    if number == 0:
        return 0

    if number == N:
        return 1

    # list 생성
    nums = [set() for _ in range(8 + 1)]
    nums[0].add(0)
    nums[1].add(N)

    # 사칙연산 결과값 추가하는 함수
    def get_result(set1, set2):
        results = set()
        for m in set1:
            for n in set2:
                results.update([m + n, m - n, m * n])
                if n != 0:
                    results.add(m // n)
        return results

    for i in range(2, 8 + 1):
        for j in range(1, i):
            nums[i].add(int(str(N) * i))
            nums[i].update(get_result(nums[j], nums[i - j]))

        if number in nums[i]:
            return i

    return -1

##################### https://gurumee92.tistory.com/164 코드
def solution(N, number):
    # 허뎝님의 수정 피드백 -> 테스트 케이스가 바뀌면서 예외 사항을 추가해야 함.
    if N == number:
        return 1

    # 1. [ SET x 8 ] 초기화
    s = [set() for x in range(8)]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    # 3. n 일반화
    #   {
    #       "n" * i U
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set,
    #    }
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer
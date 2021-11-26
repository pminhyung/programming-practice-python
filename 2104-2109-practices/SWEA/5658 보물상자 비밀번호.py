"""
(완료)

1. 수열
2. N//4씩 쪼개기 (한 변에 숫자들) -> append
3. 회전 ("1,2번" 반복)
"""

T = int(input())

for test_case in range(1, T + 1): # 각 테스트케이스
    N, K = map(int, input().split()) # N 숫자길이, K 번째 큰 숫자(비번)
    nums = input() # 수열
    nums += ' ' # line13 인덱스 에러 방지
    numall = [] # 숫자 경우의 수 

    for i in range(N//4): # 전체길이//4 만큼 회전(원래와 같아지는 회전횟수)
        temp = nums[:-1][i:] + nums[:-1][0:i] # 회전 후 수열 (앞에 것을 빼고 그만큼 뒤에 붙임, :-1 공백제거)
        numall.extend([temp[j:j+(N//4)] for j in range(0, len(temp), N//4)]) # 한변의 수열

    pw = sorted(list(set(list(map(lambda x: int(x, 16), numall)))), reverse=True)[K-1]
    print('#{} {}'.format(test_case, pw))
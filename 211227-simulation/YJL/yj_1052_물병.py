# https://velog.io/@jifrozen/Algorithm-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-1475-1052
import sys 
input = sys.stdin.readline 

N, K = map(int, input().split())
answer = 0

# N=3, K=1
# 물병 3개로 1개를 만드는 것이 불가능
# 2리터가 들어있는 물병 하나와, 1리터가 들어있는 물병 하나
# 2리터가 들어있는 물병 두 개
# 4리터가 들어있는 물병 한 개

# 3 이진수 11(2) -> 2개 만들어지는 물병 개수
# 4  100(2) -> 1개 만들어지는 물병 개수
# # 위 이진수 이용 -> 물병의 개수보다 크면 마트에서 물병 사옴
while bin(N).count('1') > K:
    # 역순으로 index가 1인 경우
    plus = 2 ** (bin(N)[::-1].index('1'))
    answer += plus
    N += plus
print(answer)
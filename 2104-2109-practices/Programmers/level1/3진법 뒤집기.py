"""
bin(n)[2:], oct()[2:], hex()[2:]
"""

# 자연수n을 i진법으로 변환하는 함수
def convert_num(n, i):
    ans = ''
    while n > 0:
        n, mod = divmod(n, i)
        ans += str(mod)
    return ans[::-1] # 나머지들을 아래서부터 쌓아나감

def solution(n):
    return int(convert_num(n,3)[::-1], 3)
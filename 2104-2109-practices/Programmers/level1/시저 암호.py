# 아스키코드 사용 (chr(), ord())

# 총 이동거리 = A로부터의 거리 + 앞으로 갈 거리
# A + (총이동거리%26)
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s)
"""
띄어쓰기 없는 input 문자열을 조심... (split과 map으로 list되지 않음)
"""
import sys
s = [int(i) for i in sys.stdin.readline().strip()]
one, zero = 0, 0
for i in range(len(s)-1):
    if (s[i], s[i+1]) == (1,0):
        one+=1
    elif (s[i], s[i+1]) == (0,1):
        zero+=1
if s[0]==0:
    one+=1
elif s[0]==1:
    zero+=1
print(min(one, zero))
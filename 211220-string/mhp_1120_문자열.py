"""
- idea : A를 B 단어 내 같은 길이의 연속된 string과 비교했을 때 최소 차이를 구함
- B에서 A 단어길이 전까지만 순회 주의
"""
import sys
a, b = sys.stdin.readline().rstrip().split()
cnts = []
for i in range(len(b)-len(a)+1):
    b_part = b[i:i+len(a)]
    cnt = 0
    for j in range(len(a)):
        if a[j]!=b_part[j]:
            cnt+=1
    cnts.append(cnt)
print(min(cnts))
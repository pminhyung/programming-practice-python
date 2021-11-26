"""
6, 9 중 하나를 서로로 대체하고, count셀 때 2로 나눠준다 (한세트에 2개 사용가능)
d[k]로 정렬 후 최대값 print
"""
import sys
from collections import Counter
nums = sys.stdin.readline().strip()
nums = nums.replace('6', '9')
nums = list(map(int,nums))
d = Counter(nums)

if 9 in d:
    if d[9]%2:
        d[9]=d[9]//2+1
    else:
        d[9]=d[9]//2

k1 = sorted(d.keys(), key= lambda x: d[x], reverse=True)[0]
print(d[k1])
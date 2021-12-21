"""
- idea : 연속된 0과 1을 한개로 치환 후 Counter 사용, 개수가 적은 숫자의 개수 반환
- 단순히 개수가 적은 숫자의 개수는 오답
- 연속된 숫자의 경우 한번에 뒤집을 수 있음
"""
import sys
from collections import Counter
import re
num = sys.stdin.readline().rstrip()
num = re.sub('0+','0', num)
num = re.sub('1+','1', num)
cnt = Counter(list(num))
print(min(list(cnt.values())) if len(cnt)!=1 else 0)

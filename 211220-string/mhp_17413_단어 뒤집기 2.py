"""
- idea : 큐 + 정규식 => 문자열 치환
- 단어 탐색 시 태그 내 단어도 해당되기 때문에 먼저 치환해줄 것
"""
from collections import deque
import sys
import re

s = sys.stdin.readline().rstrip()

tags = deque(re.findall('<[a-z\s]+>', s))
s = re.sub('<[a-z\s]+>', '*', s)

words = deque(re.findall('[\da-z]+', s))
s = re.sub('[\da-z]+', '#', s)

res = ''
for i in range(len(s)):
    if s[i] == ' ':
        res += ' '
    elif s[i] == '*':
        res += tags.popleft()
    elif s[i] == '#':
        res += words.popleft()[::-1]
print(res)

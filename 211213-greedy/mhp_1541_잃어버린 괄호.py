"""
- "-" 뒤에 괄호시작, 다음 "-"전에 괄호 닫음
- "-" 뒤에 있는 덧셈들을 모두 음수결과로
- 구현 : .split('-') / .split('+')
"""

import sys
nets = sys.stdin.readline().rstrip().split('-')
plus = sum(map(int, nets[0].split('+')))
for i in range(1, len(nets)):
    plus-=sum(map(int,nets[i].split('+')))
print(plus)
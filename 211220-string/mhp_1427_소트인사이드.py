"""
- idea : string sort 사용
- string sorted 시 list returned 주의
"""
import sys
num = sys.stdin.readline().rstrip()
print(''.join(sorted(num, reverse=True)))
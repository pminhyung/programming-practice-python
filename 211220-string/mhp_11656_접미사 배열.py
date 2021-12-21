"""
- idea : 인덱싱 + 순회
"""
import sys
word = sys.stdin.readline().rstrip()
li = [word[i:] for i in range(len(word))]
print('\n'.join(sorted(li)))

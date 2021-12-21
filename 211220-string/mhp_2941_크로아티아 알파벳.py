"""
- idea : string에서 알파벳 순차 제거 (형태가 포괄적인 순 - dz= > z=)
- 중복알파벳 존재 case 고려
- 중복 개수 n = 중복 n개 제거 후 길이변화 / 1개 제거 후 길이 변화
"""
import sys
word = sys.stdin.readline().rstrip()
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']

cnt=0
for c in li:
    before = len(word)
    word = word.replace(c, ' ')
    if before!=len(word):
        cnt+=(before-len(word))//(len(c)-1)    
cnt+=len(word.replace(' ',''))
print(cnt)
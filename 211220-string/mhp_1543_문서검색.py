"""
- idea : [idx : idx+len(unit)] 만큼 len(word)-len(unit)까지 순회하며 count
"""
import sys

inp = sys.stdin.readline
word = inp().rstrip()
unit = inp().rstrip()
idx, cnt = 0, 0
while idx <= len(word)-len(unit):
    if word[idx:idx+len(unit)] == unit:
        cnt+=1
        idx+=len(unit)
    else:
        idx+=1

print(cnt)

# replace('', '') : aaaababaa / aba : 단어를 지웠을 때 붙여진 철자끼리 단어를 이룰 수 있어 오답
# 나눗셈 사용 시 zero division case 생각하기 (unit==1일 떄 에러발생)
"""
import sys

inp = sys.stdin.readline
word = inp().rstrip()
unit = inp().rstrip()
cnt = 0 
while True:
    if unit in word:
        bef = len(word)
        word = word.replace(unit, ' ')
        cnt+=((bef-len(word))//(len(unit)-1))
        continue
    else:
        break
print(cnt)
"""
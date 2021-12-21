"""
https://computer-science-student.tistory.com/237
- idea : 연속된 문자가 아닐 때, 뒤에 string에 해당 문자가 포함되는지 check
- O(n2)

"""
N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result-=1
            break
print(result)

"""
- O(n3)

import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
cnt = 0

for _ in range(n):
    word = inp().rstrip()
    li = []
    flag=True
    
    for char in word:
        if not li:
            li.append(char)
            continue

        if char in li and char==li[-1]:
            continue

        if char in li and char!=li[-1]:
            flag=False
            break

        li.append(char)

    if flag:
        cnt+=1

print(cnt)
"""
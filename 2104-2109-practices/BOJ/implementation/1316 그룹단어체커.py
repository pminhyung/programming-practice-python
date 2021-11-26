from collections import Counter
import sys
n =int(sys.stdin.readline())
tot=0
for _ in range(n):
    s=''
    word = sys.stdin.readline().strip()
    d = Counter(word)
    for k in d:
        s+=k*d[k]

    if word==s:
        tot+=1
print(tot)
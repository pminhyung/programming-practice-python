"""
원리는 간단하나, 디테일이 은근 까다로웠던 문제

크로(크로아티아알파벳) 소거 후 공백을 남겨놔야, 따로였던 알파벳이 뭉쳐서 크로 형성 방지
소거된 크로 개수 = (공백제거된 원래word 길이 - 공백제거된 이후word길이) // (알파벳길이)

"""

import sys
sys.setrecursionlimit(10**8)

word = sys.stdin.readline().strip()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cro = sorted(cro, key= lambda x: len(x), reverse=True)

tot=0
for a in cro:
    if a in word:
        prev = len(word.replace(' ',''))
        word = word.replace(a, ' ')
        tot+=(prev-len(word.replace(' ','')))//len(a) # 공백추가므로 //2 안해도 됨
print(len(word.replace(' ','')) + tot)
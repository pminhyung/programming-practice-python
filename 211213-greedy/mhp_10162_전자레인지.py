"""
- T==0일 때 break 불가 : B, C를 사용 안할 때도 0으로 저장 및 표시해야
- if T%10!=0: return -1
"""

import sys

def get_mincnt(t, a, b, c):
    res = []
    for sec in [a,b,c]:
        # if t==0:
        #     break
        mod, t = divmod(t, sec)
        res.append(str(mod))

    if t!=0:
        return -1
    return ' '.join(res)

t = int(sys.stdin.readline())
m2s = 60
a = m2s*5
b = m2s*1
c = 10

print(get_mincnt(t, a, b, c))
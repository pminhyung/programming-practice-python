import sys
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline().strip())
h =[]

def ishansu(x):
    li = list(map(int, x))
    d=0
    for i in range(len(li)-1):
        if i==0:
            d=li[i+1]-li[i]
            continue
        if li[i+1]-li[i]!=d:
            return False
    return True

for n in range(1,N+1):
    if ishansu(str(n)):
        h.append(n)

print(len(h))
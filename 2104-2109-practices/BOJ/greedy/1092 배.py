"""
내림차순: 큰 무게의 크레인에 큰무게의 박스를 우선적으로 할당하는 것이 최소

이전시간에서 옮긴box index를 iter 하지 않도록 -> 시간초과 해결 key
start_pos에 크레인마다 시작할 box인덱스를 저장하게 하고, 다음 시간 t분에 해당 위치부터 iter 시작

"""
import sys

n = int(sys.stdin.readline().strip())
c = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
w = list(map(int, sys.stdin.readline().split()))

if max(w) > max(c):
    print(-1)
    sys.exit()

c.sort(reverse=True)
w.sort(reverse=True)

res = 0
cnt = 0

wcheck = [False] * m
start_pos = [0]*n # 1분 후 크레인이 시작할 박스 인덱스

while True:
    if cnt == m:
        break

    for i in range(len(c)):
       for j in range(start_pos[i], len(w)):
            if not wcheck[j] and c[i] >= w[j]:
                wcheck[j] = True
                start_pos[i]+=1
                cnt += 1
                break
            start_pos[i]+=1
    res += 1
print(res)
"""
- idea : deque.rotation 활용
-- 로봇여부(has_rb)와 벨트(a)를 매번 함께 회전
-- 로봇 내리기, 이동(+내리기), 올리기 를 모두 뒤에서 앞 순으로 진행 해주어야 작업 가능
"""
import sys
from collections import deque
inp = sys.stdin.readline
n, k = map(int, inp().rstrip().split())
a = deque(list(map(int, inp().rstrip().split())))
has_rb = deque([False]*(2*n))
ans = 0

# 프로세스는 상단 벨트 뒷부분부터 앞부분 순(내리기 -> 로봇이동 -> 올리기)
while True:
    ans+=1

    # 내리기
    a.rotate(1)
    has_rb.rotate(1)
    has_rb[n-1]=0

    # 로봇 이동(뒤에서 앞 순, 내리는지점 전부터), 내구도 감소
    # 이후 "내리기" 한번 더 수행
    for i in range(n-2, -1, -1):
        if has_rb[i]!=0 and has_rb[i+1]==0 and a[i+1]>0:
            has_rb[i]=0
            has_rb[i+1]=1
            a[i+1]-=1
    has_rb[n-1]=0

    # 로봇 올리기, 내구도 감소
    if a[0]>0 and has_rb[0]==0:
        has_rb[0]=1
        a[0]-=1

    # 내구도 0 count
    cnt = sum([1 for i in a if i==0])

    if cnt>=k:
        break

print(ans)
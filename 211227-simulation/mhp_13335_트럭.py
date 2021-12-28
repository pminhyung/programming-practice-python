"""
- idea: queue 활용, bridge 위의 트럭을 queue로 update하는 문제
-- waiting 트럭 존재 시 첫째 트럭과 다리 위 트럭(bridge) 무게 합 비교
-- W 이하면 보딩 아니면 dummy 추가(0)
-- 다리 위가 모두 dummy가 될 때 break
"""
import sys
from collections import deque
inp = sys.stdin.readline
N, L, W = map(int, inp().rstrip().split())
waiting = deque(list(map(int, inp().rstrip().split())))
on_bridge = deque([0]*L)

cnt = 0
while True:
    on_bridge.popleft()
    if waiting and sum(on_bridge)+list(waiting)[0]<=W :
        on_bridge.append(waiting.popleft())
    else:
        on_bridge.append(0)
    cnt+=1

    if on_bridge.count(0)==L:
        break
print(cnt)
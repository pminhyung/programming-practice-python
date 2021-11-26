"""
'우리연도 iter -> esm 표현했을 때 test case이냐?' 로 접근

임계값과 같은 값이 들어올때는 0이 되므로, (i-1)%임계값+1 을 해주면 임계값일 때도 해당 숫자를 그대로 표현할 수 있다
"""
import sys
e,s,m = map(int, sys.stdin.readline().split())

for i in range(1, 1000000):
    if ((i-1)%15+1, (i-1)%28+1, (i-1)%19+1) == (e,s,m):
        print(i)
        break
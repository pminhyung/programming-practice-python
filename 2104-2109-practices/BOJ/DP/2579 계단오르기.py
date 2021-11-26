"""
연속세칸 못뛰는 룰을 점화식으로 만들면 되었다(두칸->한칸->i) : i-3
"""
import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline().strip())

step=[]
for _ in range(n):
    step.append(int(sys.stdin.readline().strip()))

step=[False]+step
f = [False]+[step[1],step[1]+step[2]] # f(20), f(10)

idx=3
while idx<n+1: # 마지막 계단까지 구할 것
    f.append(max(f[idx-3]+step[idx-1]+step[idx],
                f[idx-2]+step[idx]))
    idx+=1
print(f[-1])
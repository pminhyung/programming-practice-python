# 재귀 사용시
def fibo(num):
    if num<=1:
        return num
    return fibo(num-1) + fibo(num-2)
print(fibo(4))

def fibo_dp(num):
    cache = [0] * (num+1)
    for i in range(len(cache)):
        if i<=1:
            cache[i] = i
        else:
            cache[i] = cache[i-1]+cache[i-2]
    return cache[-1]
print(fibo_dp(4))




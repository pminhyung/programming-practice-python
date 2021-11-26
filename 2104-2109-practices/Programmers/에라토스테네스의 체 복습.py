def sieve_of_eratosthenes(n):
    sqrt = int(n**.5) # index 0부터 시작 고려 x
    arr = ['-', False] + [True]*(n-1) # 하나씩 밀려서 노쓸모 : '-' , 1은 해당x이므로 False
    for s in range(2, sqrt+1): # sqrt(n)까지 순회하며 소수의 배수 제거, 2부터 !!
        for j in range(s*2, n+1, s):
            if arr[s] ==True: # 소수일 때만 소수의 배수들 제거
                arr[j] = False

    return sum(arr[2:]) # n포함하여 count

print(sieve_of_eratosthenes(11))
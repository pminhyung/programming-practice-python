def sieve_of_eratosthenes(n): # n이하 소수찾기
    arr = [True]*(n+1) # 포함
    sqrt = int(n**.5)
    for s in range(2, sqrt+1): # 0,1은 소수도 합성수도 X
        if arr[s]==True:
            for j in range(s*2, n+1, s):
                arr[j]=False

    print([idx for idx, b in enumerate(arr[2:], 2) if b==True])
    return sum(arr[2:]) # index 번호 수정안해서 하나씩 밀려서 원래는 [1:]이지만, 1도 제거하기 위해 (소수, 합성수X) arr[2:]

print(sieve_of_eratosthenes(11))


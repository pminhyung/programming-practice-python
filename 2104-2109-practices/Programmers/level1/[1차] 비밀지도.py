def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) # 비트연산자로 or 수행 후 출력10진수를 다시 이진변환(진법정보 제거-[2:])
        a12=a12.rjust(n,'0') # zfill, n길이만큼 나머지를 0으로 채움
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

def solution(n, arr1, arr2):
    return [str(bin(i | j)[2:]).rjust(n, '0').replace('1', '#').replace('0', ' ') for i, j in zip(arr1, arr2)]

def solution(n, arr1, arr2):
    arr = [[] for _ in range(n)]
    arr1 = list(map(lambda x: '0' * (n - len(bin(x)[2:])) + str(bin(x)[2:]), arr1))
    arr2 = list(map(lambda x: '0' * (n - len(bin(x)[2:])) + str(bin(x)[2:]), arr2))

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                arr[i].append('#')
                continue
            else:
                arr[i].append(' ')

    return [''.join(arr[i]) for i in range(n)]
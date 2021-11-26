def solution(b, y): # 24, 24
    y_yaksu = [i for i in range(1, int(y**.5)+1) if y%i==0] # 약수는 제곱근까지만 iter ( int(n**.5) 까지)

    for yi in y_yaksu:
        col = int(y/yi)+2
        row = yi+2

        if ((2*(yi+2)+(y/yi)*2) == b):
            return sorted([int(col), int(row)], reverse=True)

def solution(b, y):
    tot=b+y
    for i in range(1, int(tot**.5)+1):
        if tot%i==0: # 12 -> 2,6 or 3,4
            if (i*2 + ((tot/i)-2)*2) == b:
                return sorted(list(map(int, [i, int(tot/i)])), reverse=True)

print(int(3)==float(3))
print(solution(10,2))
print(solution(8,1))
print(solution(24,24))
print(solution(14,4))
print(solution(14,6))
print(solution(50,22))
print(solution(18,6))
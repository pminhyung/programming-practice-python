def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) # 몫-1: 따로 if문으로 뺐기 때문
        return solution(q) + '124'[r]
    return answer
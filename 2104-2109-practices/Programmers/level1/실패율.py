def solution(N, stages):
    result = {}
    num = len(stages)
    for i in range(1, N+1):
        if num!=0:
            cnt = stages.count(i)
            fail = cnt/num
            result[i] = fail
            num-=cnt
        else:
            result[i] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)


def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer
def solution(s):
    d = {'zero':0,
        'one':1,
        'two':2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine':9,
    }
    for k in d:
        s = s.replace(k, str(d[k]))
    return int(s)

s='one4seveneight'
res = solution(s)
print(res, type(res))
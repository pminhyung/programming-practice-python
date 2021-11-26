import re

def solution(dartResult):
    d = {'S': 1, 'D': 2, 'T': 3, '': 1, '*': 2, '#': -1}
    li = re.findall('(\d+)([SDT])([*#]?)', dartResult)  # [('10', 'S', '*')]

    for i in range(len(li)):
        if li[i][2] == '*' and i > 0: # i가0이면 이전원소존재X
            li[i - 1] *= 2
        li[i] = int(li[i][0]) ** d[li[i][1]] * d[li[i][2]]
    return sum(li)

def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
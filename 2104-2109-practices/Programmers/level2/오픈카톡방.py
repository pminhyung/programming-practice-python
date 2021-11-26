def solution(record):
    d = {}
    answer = []

    for sent in record:
        com, *uidname = sent.split()
        if com in 'EnterChange':
            d[uidname[0]] = uidname[1]

    for sent in record:
        com, *uidname = sent.split()
        if com == 'Enter':
            answer.append(d[uidname[0]] + '님이 들어왔습니다.')
        elif com == 'Leave':
            answer.append(d[uidname[0]] + '님이 나갔습니다.')

    return answer
def solution(s):
    """
    룰에 따라 공백 기준으로 split(' ')을 명시해주었어야 했다 (여러 공백의 문자열이 테스트케이스이기 때문)

    :param s:
    :return:
    """
    token = []
    for tok in s.split(' '):
        token.append(''.join([t.upper() if not i%2 else t.lower() for i,t in enumerate(tok)]))
    return ' '.join(token)
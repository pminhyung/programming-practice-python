def solution(s):
    return s.isdigit() and len(s) in (4, 6)

def solution(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))
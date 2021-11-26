
import sys
import re

inp = sys.stdin.readline

d = {'[':'large', ']':'large', '(':'small', ')':'small'}

def isbalanced(string):

    stack = []

    pstring = re.sub('[\.a-zA-Z\s]+', '', string)

    if pstring=='':
        print('yes')
        return

    if pstring[0] in ')]':
        print('no')
        return

    for p in pstring:
        if p == '(' or p == '[':
            stack.append(p)
            continue
        
        # stack is empty
        if not stack and (p==')' or p==']'):
            print('no')
            return
        
        # stack is not empty
        if d[p]!=d[stack[-1]]: # '[ )', '( ]' 
            print('no')
            return
        elif d[p]==d[stack[-1]]: # '[ ]', '( )'
            stack.pop()

    print('no') if stack else print('yes')

while True:
    string = inp().rstrip()
    if string=='.':
        break
    isbalanced(string)
import sys

L, C = map(int, sys.stdin.readline().split())
li = sys.stdin.readline().rstrip().split()

mmm = {'a', 'e', 'i', 'o', 'u'}
mo = set.intersection(mmm, set(li))
ja = set(li) - mmm

q = set()
pw = set()

for m in mo:
    q.add(m)

def bfs():
    while q:
        step = q.pop()
        if len(step) == 1 or len(step) == 2:
            for j in ja:
                if j not in step:
                    q.add(''.join(sorted(step+j)))
            continue

        if len(step) == L:
            pw.add(''.join(sorted(step)))
            continue

        for letter in li:
            if letter not in step:
                q.add(''.join(sorted(step+letter)))
bfs()
#print(pw)
print('\n'.join(pw))
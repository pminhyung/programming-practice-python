"""
f string {변수명:.0f} - 0을 써줘야.
"""
from collections import Counter
import sys

n = int(sys.stdin.readline().rstrip())
data = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
data.sort()


def get_mode(data):
    d = Counter(data)
    highest = max(d.values())

    modes = []

    for k in d:
        if d[k] == highest:
            modes.append(k)

    if len(modes) == 1:
        return modes[0]
    else:
        return sorted(modes)[1]


stats = []
stats.append(f"{sum(data) / len(data):.0f}")
stats.append(data[len(data) // 2])
stats.append(get_mode(data))
stats.append(data[-1] - data[0] if data[-1] - data[0] >= 0 else -(data[-1] - data[0]))

for i in range(4):
    print(stats[i])
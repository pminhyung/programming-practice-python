# O(n)
import random
# li = [random.randint(1,100) for i in range(10)]
# print(li)
li = [43, 63, 61, 13, 79, 27, 71, 51, 3, 25]

def sequential_search(data, search):
    for i in range(len(data)):
        if data[i]==search:
            return i
    return False

print(sequential_search(li, 51))
print(sequential_search(li, 50))
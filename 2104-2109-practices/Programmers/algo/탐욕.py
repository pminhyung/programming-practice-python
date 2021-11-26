# 동전문제
total = 4720
coins = [1, 50, 100, 500]
def min_coin(total, coins):
    cnts = []
    for i in sorted(coins, reverse=True):
        cnt = total//i
        cnts.append(cnt)
        total -= i*cnt
    return sum(cnts)

print(min_coin(total, coins))

#부분배낭문제
data_list = [(10,10), (15,12), (20,10), (25,8), (30,5)]
def max_value(data_list, capacity):
    li = sorted(data_list, key= lambda x: x[1]/x[0], reverse=True)
    value = 0
    detail = []
    for data in li:
        if capacity >= data[0]:
            capacity-=data[0]
            value+=data[1]
            detail.append((data[0], data[1], 1))
        else:
            value+=data[1]*(capacity/data[0])
            detail.append((data[0], data[1], (capacity/data[0])))
            break
    return value, detail

print(max_value(data_list, 30))
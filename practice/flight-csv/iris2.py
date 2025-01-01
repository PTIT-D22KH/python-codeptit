import csv
data = []

with open("flights.csv", 'r') as file:
    reader = csv.reader(file)
    data = [i for i in reader]
cols = data[0]
col_num = {}
count = 0
for x in cols:
    col_num[x] = count
    count += 1
# print(col_num)
data = data[1:]

def calMin(species, col):
    min = 10**9
    for x in data:
        if x[4] == species:
            print(float(x[col_num[col]]))
            if (float(x[col_num[col]]) < min):
                min = x[col_num[col]]
    if min == 10**9:
        return -1
    return min

def calMax(species, col):
    max = 0
    for x in data:
        if x[4] == species:
            if (float(x[col_num[col]]) > max):
                max = float(x[col_num[col]])
    if max == 0:
        return -1
    return max
def calSum(species, col):
    sum = 0
    for x in data:
        if x[4] == species:
            sum += float(x[col_num[col]])
    if sum == 0:
        return -1
    return sum

def calAvg(species, col):
    sum = 0
    count = 0
    for x in data:
        if x[4] == species:
            sum += float(x[col_num[col]])
            count += 1
    if sum == 0:
        return -1
    return sum/count

for _ in range(int(input())):
    a = input().split()
    species = a[0]
    col = a[1]
    type = a[2]
    # print(data)
    if col not in col_num:
        # print("NOt column")
        print("Invalid")
        continue
    if type == 'min':
        res = calMin(species, col)
        if (res == -1):
            print("Invalid")
            continue
        print(res)
    elif type == 'max':
        res = calMax(species, col)
        if (res == -1):
            print("Invalid")
            continue
        print(res)
    elif type == 'avg':
        res = calAvg(species, col)
        if (res == -1):
            print("Invalid")
            continue
        print(res)
    else:
        res = calSum(species, col)
        if (res == -1):
            print("Invalid")
            continue
        print(res)

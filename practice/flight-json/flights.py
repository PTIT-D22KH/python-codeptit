import json



with open("flights.json", 'r') as file:
    s = json.load(file)
data = s['flights']

def calSum(year):
    sum = 0
    for x in data:
        if x['year'] == year:
            sum += int(x['passengers'])
    return sum

def calMin(year):
    min = 1e9
    for x in data:
        if x['year'] == year and int(x['passengers']) < min:
            min = int(x['passengers'])
    return min

def calMax(year):
    max = 0
    for x in data:
        if x['year'] == year and int(x['passengers']) > min:
            max = int(x['passengers'])
    return max

def calAvg(year):
    sum = 0
    count = 0
    for x in data:
        if x['year'] == year:
            sum += int(x['passengers'])
            count += 1
    return sum/count

for _ in range(int(input())):
    a = input().split()
    year = a[0]
    type = a[1]
    if (type == 'sum'):
        print(calSum(year))
    elif type == 'min':
        print(calMin(year))
    elif type == 'max':
        print(calMax(year))
    else:
        print(f"{calAvg(year):.5f}")

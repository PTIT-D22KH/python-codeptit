import json
data = None
with open("flights.json", 'r') as file:
    data = json.load(file)
data = data['flights']

for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    sum = 0
    for a in data:
        if (int(a['year']) >= x and int(a['year']) <= y):
            sum += int(a['passengers'])
    if (sum == 0):
        print("Invalid")
        continue
    print(sum)

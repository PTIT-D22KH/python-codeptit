import csv

data = []
with open ("flights.csv", 'r') as file:
    reader = csv.reader(file)
    for x in reader:
        data.append(x)
data = data[1:]
for _ in range(int(input())):
    a = input().split()
    type = a[0]
    petal_length = a[1]
    sum = 0
    count = 0
    for x in data:
        if (x[4] == type and x[2] == petal_length):
            sum += float(x[3])
            count += 1
    if count == 0:
        print("Invalid")
        continue
    else:
        print(f"{sum/count:.2f}")
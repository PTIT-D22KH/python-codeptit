import csv
data = []
with open("flights.csv", 'r') as file:
    reader = csv.reader(file)
    data = [i for i in reader]
data = data[1:]
print(data)
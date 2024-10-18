import csv

file_name = 'data.csv'

fields = []
rows = []
with open(file_name, "r")  as file:
    csv_reader = csv.reader(file)
    fields = next(csv_reader)

    for row in csv_reader:
        rows.append(row)
print(fields)
for row in rows:
    print(row)
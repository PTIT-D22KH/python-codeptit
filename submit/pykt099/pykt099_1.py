a = []
b = []
with open("DATA1.in", 'r') as file:
    s = file.readlines()
for x in s:
    for y in x.split():
        y = y.lower()
        if y not in a:
            a.append(y)
with open("DATA2.in", 'r') as file:
    s = file.readlines()
for x in s:
    for y in x.split():
        y = y.lower()
        if y not in b:
            b.append(y)
c = []
d = []
for x in a:
    if x not in b:
        c.append(x)
for x in b:
    if x not in a:
        d.append(x)
c.sort()
d.sort()
for x in c:
    print(x, end = ' ')
print()
for x in d:
    print(x, end = ' ')


        


d = {}
with open("CONTACT.in", "r") as file:
    a = file.readlines()
for x in a:
    x = x.strip().lower()
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
res = sorted(d, key = lambda x : x)
for x in res:
    print(x)   

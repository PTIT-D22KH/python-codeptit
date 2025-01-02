import re
s = ""
while True:
    t = input().strip().lower()
    if not t:
        break
    s += t + " "
print(s)

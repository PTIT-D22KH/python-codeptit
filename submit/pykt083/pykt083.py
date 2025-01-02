d = {"Xe_con":{5:10000, 7:15000}, "Xe_khach":{29:50000, 45:70000}, "Xe_tai": 20000}
# print(type(d) == dict)
res = {}
for _ in range(int(input())):
    s = input().split()
    # print(s)
    if (s[3] == "IN"):
        # print(s)
        if (type(d[s[1]]) == dict):
            # print(s)
            if s[4] not in res:
                res[s[4]] = d[s[1]][int(s[2])]
            else:
                res[s[4]] += d[s[1]][int(s[2])]
        else:
            if s[4] not in res:
                res[s[4]] = d[s[1]]
            else:
                res[s[4]] += d[s[1]]
for key, value in res.items():
    print(f"{key}: {value}")
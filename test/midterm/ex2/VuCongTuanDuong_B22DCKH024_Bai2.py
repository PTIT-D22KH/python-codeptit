res = []
b = []
max_length_res = []
max_length = 0

def solve(l, a):
    global max_length
    for j in range(l, len(a)):
        if l == 0 or a[j] >= a[l - 1]:
            b.append(a[j])
            max_length = max(max_length, len(b))
            res.append(b[:])
            solve(j + 1, a)
            b.pop()

def formatNum(x):
    if x.is_integer():
        return int(x)
    return x

a = [float(i) for i in input("Nhap mang:").split()]
n = len(a)
solve(0, a)
print(f"Tong so cach: {len(res)}")
for x in res:
    x = [formatNum(i) for i in x]
    if len(x) == max_length:
        max_length_res.append(x)
    print(x)
print(f"K nho nhat = {n - max_length}")
for x in max_length_res:
    print(x)
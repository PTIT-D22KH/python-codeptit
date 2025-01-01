n = int(input())
a = []
for _ in range(n):
    a.append([int(i) for i in input().split()])
sumUpper = 0
sumLower = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            sumUpper += a[i][j]
        elif i + j >= n:
            sumLower += a[i][j]
k = int(input())
diff = abs(sumUpper - sumLower)
if diff <= k:
    print("YES")
    print(diff)
else:
    print("NO")
    print(diff)

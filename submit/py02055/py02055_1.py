import math
import decimal
from decimal import Decimal
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n,m = [int(i) for i in input().split()]

a = []
for _ in range(n):
    a.append([int(i) for i in input().split()])
maxValue = 0
for x in a:
    for y in x:
        if (isPrime(y) and y > maxValue):
            maxValue = y
if (maxValue == 0):
    print("NOT FOUND")

else:
    print(maxValue)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxValue:
                print(f"Vi tri [{i}][{j}]")
print(Decimal("6.654").quantize(Decimal("0.01"), decimal.ROUND_HALF_UP))
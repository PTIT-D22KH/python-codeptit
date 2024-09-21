import math
size = 1000 + 1
era = [1] * size
primes = []
def sieve(size):

    era[0] = 0
    era[1] = 0
    for i in range(2, size):
        if era[i] == 1:
            for j in range(i * i, size, i):
                era[j] = 0
            primes.append(i)

sieve(size)
# print(primes)
n, m = [int(i) for i in input().split()]
a = []
# print(n, m)
for _ in range(n):
    temp = [int(i) for i in input().split()]
    # print(temp)
    a.append(temp)
# print(a)
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end = ' ')
#     print()
for i in range(n):
    for j in range(m):
        if a[i][j] not in primes:
            a[i][j] = 0
        else:
            a[i][j] = 1
        print(a[i][j], end = ' ')
    print()


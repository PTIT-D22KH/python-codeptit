import math

def sieve(a):
    a[0] = False
    a[1] = False
    for i in range(int(math.sqrt(10000)) + 1):
        if a[i] == True:
            for j in range(i + i, 10001, i):
                a[j] = False
    prime = []
    for i in range(2, 10001):
        if a[i] == True:
            prime.append(i)  # Append the index i, not a[i]
    return prime

def main():
    # Read input values
    n, x = [int(i) for i in input().split()]
    a = [True] * 10001
    prime = sieve(a)
    print(x, end=' ')
    for i in range(n):
        print(x + (i + 1) * prime[i], end=' ')

if __name__ == '__main__':
    main()
# py02031.py
import math
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True
def main():
    # Write your code here
    n, m = [int(i) for i in input().split()]
    a = [[0] * m] * n
    # print(a)
    for i in range(n):
        b = [int(i) for i in input().split()]
        for x in b:
            if (isPrime(x)):
                print("1", end = ' ')
            else:
                print("0", end = ' ')
        print()


if __name__ == '__main__':
    main()

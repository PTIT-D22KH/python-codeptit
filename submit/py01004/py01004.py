# py01004.py
import math
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True
def testCase() :
    n = int(input())
    count = 0
    for i in range(1, n):
        if (gcd(i, n) == 1):
            count += 1
    if (isPrime(count) == True):
        print("YES")
    else:
        print("NO")
    
def main():
    # Write your code here
    t = int(input())
    while t > 0:
        testCase()
        t -= 1


if __name__ == '__main__':
    main()

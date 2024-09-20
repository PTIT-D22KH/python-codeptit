# py02028.py
import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def main():
    # Write your code here
    n = int(input())
    a = [int(i) for i in input().split()]
    prime = [i for i in a if isPrime(i)]
    not_prime = [i for i in a if not isPrime(i)]
    prime.sort()
    currPrime  = 0
    # currNormal = 0
    for i in range(len(a)):
        if not isPrime(a[i]):
            print(a[i], end = ' ')
        else:
            print(prime[currPrime], end = ' ')
            currPrime += 1

if __name__ == '__main__':
    main()

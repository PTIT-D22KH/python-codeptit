# py01049.py
import math
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True
def check(s):
    l = len(s)
    if(isPrime(l) == False):
       return False
    countPrime = 0
    for c in s:
        if(isPrime(int(c))):
            countPrime += 1
    if (countPrime > l - countPrime):
        return True
    return False
    
def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        if (check(s)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

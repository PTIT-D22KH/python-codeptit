# py01057.py
import math
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True
def check(n):
    l = len(n)
    for i in range(l):
        if ((isPrime(i) and isPrime(int(n[i]))) or (isPrime(i) == False and isPrime(int(n[i])) == False)):
            continue
        else:
            return False
    return True
def main():
    # Write your code here
    for t in range(int(input())):
        n = input()
        if (check(n)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

# py01061.py
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
    for t in range(int(input())):
        n = input()
        a = int(n[:3])
        b = int(n[-3:])
        if (isPrime(a) and isPrime(b)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

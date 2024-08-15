# py01052.py
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
        sumDigits = 0
        for c in n:
            sumDigits += int(c)
        if (isPrime(int(sumDigits))) :
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

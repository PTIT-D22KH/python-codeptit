# py01056.py
import math
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True
def check(n):
    sumDigits = 0
    for i in range(len(n)):
        if ((i % 2 == 0 and int(n[i]) % 2 == 0) or (i % 2 == 1 and int(n[i]) % 2 == 1)):
            sumDigits += int(n[i])
        else:
            return False
    if (isPrime(sumDigits)) :
        return True
    return False
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

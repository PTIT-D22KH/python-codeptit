# icpc0114.py
import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def check(n):
    reversed_n = n[::-1]
    sumDigits =0 
    for c in n:
        if (not isPrime(int(c))):
            return False
        sumDigits += int(c)
    if (isPrime(int(n)) and isPrime(int(reversed_n)) and isPrime(sumDigits)):
        return True
    return False

def main():
    # Write your code here
    for t in range(int(input())):
        if (check(input())):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

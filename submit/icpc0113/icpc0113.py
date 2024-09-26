# icpc0113.py
import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def check(n):
    x = str(n)
    reversed_x = x[::-1]
    if (x == reversed_x):
        return False
    return (isPrime(n) and isPrime(int(reversed_x)))
def main():
    # Write your code here
    for t in range(int(input())):
        n = int(input())
        for i in range(10, n + 1):
            reversed_i = int(str(i)[::-1])
            if (reversed_i > i and reversed_i <= n and check(i)):
                print(i, end = ' ')
                print(reversed_i, end = ' ')
        print()
        

if __name__ == '__main__':
    main()

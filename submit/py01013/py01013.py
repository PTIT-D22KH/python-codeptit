# py01013.py
import math
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
def sumDigits(x):
    sum =0 
    while (x > 0):
        sum += int(x % 10)
        x /= 10
    # print("sum: " , sum)
    return sum
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
        s = input()
        a, b = [int(x) for x in s.split(" ")] 
        # a = int(input())
        # b = int(input())
        if(isPrime(sumDigits(gcd(a,b))) == True):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

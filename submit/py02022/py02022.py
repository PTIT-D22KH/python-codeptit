# py02022.py
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
    res = {}
    for x in a:
        if isPrime(x) :
            if x not in res.keys():
                res[x] = 1
            else:
                res[x] += 1
    for x, fre in res.items():
        print(f"{x} {fre}")
    

if __name__ == '__main__':
    main()

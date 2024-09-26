# py02030.py
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
    b = []
    seen = set()

    for x in a:
        if x not in seen:
            seen.add(x)
            b.append(x)
    total_sum = sum(b)
    currSum = 0
    for i in range(len(b)):
        currSum += b[i]
        remain_sum = total_sum - currSum
        if isPrime(currSum) and isPrime(remain_sum):
            print(i)
            return
    print("NOT FOUND")

if __name__ == '__main__':

    main()

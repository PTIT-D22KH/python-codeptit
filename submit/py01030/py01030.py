# py01030.py
import math
def main():
    # Write your code here
    n, k = [int(i) for i in input().split()]
    count = 0
    for i in range(10**(k - 1), 10**k):
        if (math.gcd(n, i) == 1):
            print(i, end = " " )
            count += 1
            if(count == 10):
                print()
                count = 0
    


if __name__ == '__main__':
    main()

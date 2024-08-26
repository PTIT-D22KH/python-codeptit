# py02019.py
import math
def main():
    # Write your code here
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(n):
        for j in range(i + 1, n):
            if (math.gcd(a[i], a[j]) == 1):
                print(f"{a[i]} {a[j]}")

if __name__ == '__main__':
    main()

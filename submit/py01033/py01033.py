# py01033.py
import math
def main():
    # Write your code here
    l, r = [int(i) for i in input().split()]
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            for k in range(j + 1, r + 1):
                if(math.gcd(i, j) == 1 and math.gcd(i, k) == 1 and math.gcd(j, k) == 1):
                    print(f"({i}, {j}, {k})")

if __name__ == '__main__':
    main()

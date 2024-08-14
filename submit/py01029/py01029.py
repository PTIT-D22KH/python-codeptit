# py01029.py
import math

def testCase():
    n = input()
    reversed_n = n[::-1]
    x = int(n)
    reversed_x = int(reversed_n)
    # print(x, reversed_x)
    if (math.gcd(x, reversed_x) == 1):
        print("YES")
    else:
        print("NO")
def main():
    # Write your code here
    for t in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()

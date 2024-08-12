# py01003.py
import math
def testCase() :
    n = input()
    # print(n)
    length = len(n)
    x = int(n)
    x /= 10**(length - 1)
    # print(x)
    # print(x - int(x))
    if (x - int(x) >= 0.5):
        x = int(x) + 1
    else:
        x = int(x)
    print(x * (10 ** (length - 1)))
def main():
    # Write your code here
    t = int(input())
    while (t > 0) :
        testCase()
        t -= 1;

    

if __name__ == '__main__':
    main()

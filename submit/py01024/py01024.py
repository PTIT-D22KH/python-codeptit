# py01024.py
import math
def testCase() :
    s = input()
    sumDigits = 0
    for i in range(len(s) - 1):
        sumDigits += int(s[i])
        if (abs(int(s[i + 1]) - int(s[i])) != 2):
            print("NO")
            return
    sumDigits += int(s[-1])
    if (sumDigits % 10 == 0):
        print("YES")
    else:
        print("NO")

def main():
    # Write your code here
    for t in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()

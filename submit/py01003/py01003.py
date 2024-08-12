# py01003.py
import math
def testCase() :
    list_digit = [int(i) for i in input()]
    for i in range(len(list_digit) - 1, 0, -1):
        if (list_digit[i] >= 5):
            list_digit[i - 1] += 1
        list_digit[i] = 0
    for i in list_digit:
        print(i, end="")
    print()
def main():
    # Write your code here
    t = int(input())
    while (t > 0) :
        testCase()
        t -= 1;

    

if __name__ == '__main__':
    main()

# py01023.py
import math
def testCase():
    n = int(input())
    print("1", end="")
    
    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0
        while(n % i == 0):
            count += 1
            n /= i
        if (count != 0):
            print(f" * {int(i)}^{count}", end = "")
        
    if (n > 1):
        print(f" * {int(n)}^{1}", end = "")
    print()
def main():
    # Write your code here
    for t in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()

# py01006.py
def testCase():
    n = input()
    for c in n:
        if ((c != '4') & (c != '7')):
            print("NO")
            return
    print("YES")
def main():
    # Write your code here
    t = int(input())
    while t > 0:
        testCase()
        t -= 1

if __name__ == '__main__':
    main()

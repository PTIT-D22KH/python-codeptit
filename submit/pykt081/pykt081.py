# pykt081.py
def testCase():
    a = input().strip().split(".")
    for x in a:
        if (int(x) < 0 or int(x) > 255):
            print("NO")
            return
    print("YES")
def main():
    # Write your code here
    for _ in range(int(input())):
        testCase()
        

if __name__ == '__main__':
    main()

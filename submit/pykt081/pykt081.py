# pykt081.py
def testCase():
    s = input().split(".")
    if (len(s) != 4):
        print("NO")
        return
    for x in s:
        if not x.isdigit():
            print("NO")
            return
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

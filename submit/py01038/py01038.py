# py01038.py
def testCase():
    res = 0
    n = int(input())
    if (n % 7 == 0):
        print(n)
        return
    for i in range(1000):
        res = n + int(str(n)[::-1])
        if (res % 7 == 0):
            print(res)
            return
        n = res
    print("-1")
def main():
    # Write your code here
    for t in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()

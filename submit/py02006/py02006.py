def testCase():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            return
    print("YES")

def main():
    for t in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()
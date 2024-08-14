# py01041.py
def findIndex(n):
    for i in range(1, len(n)):
        if (n[i] == n[i - 1]):
            return -1
        if (n[i] < n[i - 1]):
            return i
    return -1 
def testCase():
    n = input()
    if (len(n) < 3):
        print("NO")
        return
    index = findIndex(n)
    if index == -1:
        print("NO")
        return
    for i in range(index + 1, len(n)):
        if (n[i] > n[i - 1]):
            print("NO")
            return
    print("YES")

def main():
    # Write your code here
    for t in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()

# py02071.py
def Try(n, max_num, currList, res):
    if n == 0:
        res.append(currList[:])
        return
    for i in range(min(n, max_num), 0, -1):
        currList.append(i)
        Try(n - i, i, currList, res)
        currList.pop()
def testCase():
    n = int(input())
    res = []
    Try(n, n, [], res)
    print(len(res))
    for x in res:
        print(f"({' '.join(map(str, x))})", end = ' ')
    print()
    

def main():
    # Write your code here
    for _ in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()

# py01043.py
def check(p):
    for c in p:
        if (int(c) % 2 == 1):
            return False
    return True
def genPalindromes(limit):
    res = []
    for length in range(2, len(str(limit)) + 1, 2):
        m = length // 2
        start = 10 ** (m  - 1)
        end = 10 ** m
        for i in range(start, end):
            s = str(i)
            palindrome = s + s[::-1]
            if (int(palindrome) < limit):
                res.append(palindrome)
    return res
def testCase() :
    n = int(input())
    res = genPalindromes(n)
    for p in res:
        if ((check(p))):
            print(p, end = ' ')

    
def main():
    # Write your code here
    for t in range(int(input())):
        testCase()
        print()

if __name__ == '__main__':
    main()

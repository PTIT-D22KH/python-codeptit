# py03013.py
def countFunction(x, n):
    res = 0
    for i in range(0, 10):
        digitPlace = 10 ** i
        if digitPlace > n:
            break
        completeSets = n // digitPlace
        remainder = n % digitPlace
        currDigit = completeSets % 10

        if currDigit > x:
            res += ((completeSets // 10) + 1) * digitPlace
        elif currDigit == x:
            res += (completeSets // 10) * digitPlace + (remainder + 1)
        else:
            res += (completeSets // 10) * digitPlace
        if x == 0:
            res -= digitPlace
    return res

def countDigits(d, low, high):
    return countFunction(d, high) - countFunction(d, low - 1)
def main():
    # Write your code here
    for _ in range(int(input())):
        a, b= [int(i) for i in input().split()]
        for i in range(0, 10):
            print(countDigits(i, a, b), end = ' ')
        print()

if __name__ == '__main__':
    main()

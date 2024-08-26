# py02024.py
class Number:
    def __init__(self, value) -> None:
        self.value = value
        productDigits = 1
        x = self.value
        while (x > 0):
            productDigits *= (x % 10)
            x = x // 10
        self.productDigits = productDigits
def cmp(a):
    return (a.productDigits, a.value)

def main():
    # Write your code here
    for t in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        res = []
        for x in a:
            res.append(Number(x))
        res.sort(key = cmp)
        for x in res:
            print(x.value, end = ' ')
        print()

if __name__ == '__main__':
    main()

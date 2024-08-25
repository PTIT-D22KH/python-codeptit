# py02009.py
class Data:
    def __init__(self, value, fre):
        self.value = value
        self.fre = fre

def cmp(a):
    return (a.fre * (-1), a.value)
        
def main():
    # Write your code here
    for t in range(int(input())):
        n = int(input())
        a = []
        b = []
        d = dict()
        for j in range(n):
            x = int(input())
            if x not in a:
                a.append(x)
                d[x] = 0
            else:
                d[x] += 1
        for x in a:
            b.append(Data(x, d[x]))
        b.sort(key = cmp)
        print(b[0].value)

if __name__ == '__main__':
    main()

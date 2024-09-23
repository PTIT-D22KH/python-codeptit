class Number:
    def __init__(self, rank, value, fre) -> None:
        self.rank = rank
        self.value = value
        self.fre = fre
    
    def __str__(self) -> str:
        return str(self.value) + " " + str(self.fre)

def cmp(a):
    return a.value

def main():
    s = input().strip()
    k = int(input())
    a = []
    b = set()
    c = []
    d = {}
    
    for i in range(0, len(s) - 1, 2):
        t = s[i:i+2]
        x = int(t)
        b.add(x)
        c.append(x)
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    
    curr = 0
    for x in c:
        if x in b:
            n = Number(curr, x, d[x])
            curr += 1
            a.append(n)
            b.remove(x)
    
    a.sort(key=cmp)
    ok = False
    for x in a:
        if x.fre >= k:
            print(str(x))
            ok = True
    if not ok:
        print("NOT FOUND")

if __name__ == '__main__':
    main()
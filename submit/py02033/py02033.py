# py02032.py
class Number:
    def __init__(self, rank, value) -> None:
        self.rank = rank
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)

def cmp(a):
    return (a.rank)

def main():
    # Write your code here
    s = input()
    a = []
    b = set()
    c = []
    for i in range(0, len(s), 2):
        if i + 2 < len(s):
            t = s[i:i+2]
        b.add(int(t))
        c.append(int(t))
    curr = 0
    for x in c:
        if x in b:
            n = Number(curr, x)
            curr += 1
            a.append(n)
            b.remove(x)
    # a = list(a)
    a.sort(key = cmp)
    for x in a:
        print(str(x), end = ' ')

if __name__ == '__main__':
    main()

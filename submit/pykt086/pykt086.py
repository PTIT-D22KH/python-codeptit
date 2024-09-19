def toS(i):
    if i <= 9:
        return str(i)
    return chr(ord('A') + i - 10)

def convert(s):
    r = 0
    for i in s:
        r = r * 2 + int(i)
    return toS(r)

def main():
    with open('pykt086/DATA.in', 'r') as f:
        # T = int(f.readline().strip())
        for _ in range(int(f.readline().strip())):
            b = int(f.readline().strip())
            s = f.readline().strip()
            r = ''
            while s:
                r = convert(s[-b:]) + r
                s = s[:-b]
            print(r)

if __name__ == '__main__':
    main()
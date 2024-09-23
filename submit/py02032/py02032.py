# py02032.py

def main():
    # Write your code here
    s = input()
    a = set()
    for i in range(0, len(s), 2):
        if i + 2 < len(s):
            t = s[i:i+2]
        a.add(int(t))
    a = list(a)
    a.sort()
    for x in a:
        print(x, end = ' ')

if __name__ == '__main__':
    main()

# py02027.py

def main():
    # Write your code here
    a = []
    for _ in range(int(input())):
        s = input()
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            else:
                if len(num) != 0:
                    a.append(int(num))
                    num = ""
        if len(num) != 0:
            a.append(int(num))
    a.sort()
    for x in a:
        print(x)

if __name__ == '__main__':
    main()

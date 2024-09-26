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
        if len(num) != 0:
            a.append(num)

if __name__ == '__main__':
    main()

# py01017.py

def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        s = s + "."
        res = ""
        count = 0
        curr = s[0]
        for c in s:
            if (c == curr):
                count += 1
            else:
                res = res + str(count) + curr
                curr = c
                count = 1
        print(res)


if __name__ == '__main__':
    main()

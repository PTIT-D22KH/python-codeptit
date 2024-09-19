# py01021.py
def solve(s):
    x = ''
    sum = 0
    for c in s:
        if (c.isdigit()):
            sum += int(c)
        else:
            x += c
    # x.sort()
    return ''.join(sorted(x)) + str(sum)

def main():
    # Write your code here
    for _ in range(int(input())):
        s = input()
        print(solve(s))

if __name__ == '__main__':
    main()

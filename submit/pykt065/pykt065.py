# pykt065.py
def check(i, n):
    for x in range(2, n + 1):
        if (i % x == 0):
            return False
    return True
def main():
    # Write your code here
    while True:
        s = input()
        # print(s)
        if (s == '-1'):
            break
        else:
            l, r = [int(i) for i in s.split()]
            n = int(input())
            # print("n", n)
            res = 0
            for i in range(l, r + 1):
                if (check(i, n)):
                    res += 1
            print(res)



if __name__ == '__main__':
    main()

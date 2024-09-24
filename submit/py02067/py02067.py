# py02067.py
def check(p, a):
    for x in a:
        if int(x / p) == int(x / (p + 1)):
            return False
    return True
def main():
    # Write your code here
    n = int(input())
    a = [int(i) for i in input().split()]
    end = min(a)
    res = 0
    for i in range(end, 0, -1):
        if (check(i, a)):
            for j in range(n):
                ans += int(a[j] / (i + 1)) + 1
            break
    print(res)

if __name__ == '__main__':
    main()

# icpc0100.py
def solve(a, n):
    res = 0
    for i in range(n - 1):
        x, y = a[i], a[i + 1]
        while (max(x, y) > 2 * min(x, y)):
            if x < y:
                x *= 2
            else:
                y *= 2
            res += 1
    return res

def main():
    # Write your code here
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(solve(a,n))


if __name__ == '__main__':
    main()

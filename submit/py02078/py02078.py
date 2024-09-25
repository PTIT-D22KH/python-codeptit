# py02078.py

def main():
    # Write your code here
    for _ in range(int(input())):
        n = int(input())
        a = []
        b = []
        for _ in range(n):
            x, y = [float(i) for i in input().split()]
            a.append(x)
            b.append(y)
        # a = [float(i) for i in input().split()]
        # b = [float(i) for i in input().split()]
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if a[j] < a[i] and b[j] > b[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))


if __name__ == '__main__':
    main()

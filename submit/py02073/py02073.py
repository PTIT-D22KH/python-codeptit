# py02073.py
def solve(n, x, y, z):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    dp[1] = x
    for i in range(2, n + 1):
        #insert
        dp[i] = dp[i - 1] + x

        #copy
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + z)
        else:
            dp[i] = min(dp[i], dp[(i + 1) // 2] + z + y)
    return dp[n]

def testCase():
    n = int(input())
    x,y,z = [int(i) for i in input().split()]
    print(solve(n, x,y,z))

def main():
    # Write your code here
    for _ in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()

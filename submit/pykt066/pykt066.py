# pykt066.py
import math
def solve(a,n , k):
    min_length = float('inf')
    for i in range(n):
        curr_gcd = a[i]
        if curr_gcd == k:
            min_length = min(min_length, 1)
        for j in range(i + 1, n):
            curr_gcd = math.gcd(curr_gcd, a[j])
            if curr_gcd == k:
                min_length = min(min_length, j - i + 1)
                break
    if min_length == float('inf'):
        return -1
    return min_length

def testCase():
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    print(solve(a, n, k))
def main():
    # Write your code here
    for _ in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()

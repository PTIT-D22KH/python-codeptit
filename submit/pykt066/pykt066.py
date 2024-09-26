import math

def solve(a, n, k):
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

def process_test_cases(e, I):
    n, k = e[I], e[I+1]
    I += 2
    a = e[I:I+n]
    I += n
    result = solve(a, n, k)
    print(result)
    return I

def main():
    t = int(input())
    e = []
    while True:
        try:
            e.extend(map(int, input().split()))
        except:
            break
    I = 0
    for _ in range(t):
        I = process_test_cases(e, I)

if __name__ == '__main__':
    main()
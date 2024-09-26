# py02014.py
def sieve():
    for i in range(2, 10001):
        if a[i] == 1:
            for j in range(i * i, 10001, i):
                a[j] = 0
            b.append(i)

def main():
    # Write your code here
    n = int(input())
    x = [int(i) for i in input().split()]
    ans = 0
    for c in x:
        s = 10**9
        for prime in b:
            s = min(s, abs(c - prime))
        ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    global a
    a = [1] * 10001
    global b
    b = []
    sieve()
    main()

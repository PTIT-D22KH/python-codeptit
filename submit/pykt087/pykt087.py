# pykt087.py
def specialNumber(n, k):
    res = 0
    power = 1
    while k > 0:
        if k % 2 == 1:
            res = (res + power) % MOD
        power = (power * n) % MOD
        k //= 2
    return res


def main():
    # Write your code here
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        print(specialNumber(n, k))

if __name__ == '__main__':
    global MOD 
    MOD = int(1e9 + 7)
    main()

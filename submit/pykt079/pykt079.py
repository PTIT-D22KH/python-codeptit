# pykt079.py

def main():
    # Write your code here
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        min_val = min(a)
        max_val = max(a)
        res = 0
        for i in range(min_val, max_val + 1):
            if i not in a:
                res += 1
        print(res)

if __name__ == '__main__':
    main()

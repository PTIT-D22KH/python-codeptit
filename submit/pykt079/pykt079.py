# pykt079.py

def main():
    # Write your code here
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        m = min(a)
        n = max(a)
        print(n - m + 1 - len(a))

if __name__ == '__main__':
    main()

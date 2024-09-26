# py02011.py

def main():
    # Write your code here
    n = int(input())
    a = [int(i) for i in input().split()]
    b = list(set(a))
    res = float('inf')
    ans = 0
    for x in b:
        steps = sum(abs(i - x) for i in a)
        if steps < res:
            res = steps
            ans = x
        elif steps == res:
            if (a.index(x) < a.index(ans)):
                ans = x
    print(f"{res} {ans}")

if __name__ == '__main__':
    main()

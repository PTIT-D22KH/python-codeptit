# py02048.py

def main():
    # Write your code here
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    count = 1
    for i in range(1, n):
        if a[i] - a[i - 1] > k:
            count += 1
    print(count)

if __name__ == '__main__':
    main()

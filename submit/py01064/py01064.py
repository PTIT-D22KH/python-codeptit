# py01064.py
def find(n, k):
    if n == 1:
        return 'A'
    length_previous = (2 ** (n - 1)) - 1
    mid = length_previous + 1

    if k == mid:
        return chr(n + 64)
    elif k < mid:
        return find(n - 1, k)
    else:
        return find(n - 1, k - mid)

def main():
    # Write your code here
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        print(find(n, k))

if __name__ == '__main__':
    main()

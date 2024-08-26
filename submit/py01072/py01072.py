# py01072.py
def Try(i):
    if len(res) == k:
        for num in res:
            print(num, end=' ')
        print()
        return
    for j in range(i, n):
        res.append(a[j])
        Try(j + 1)
        res.pop()

def main():
    global n, k, a, res
    n, k = [int(i) for i in input().split()]
    a = set()
    s = input()
    for i in s.split():
        a.add(int(i))
    a = sorted(list(a))  # Sort the list to ensure lexicographical order
    n = len(a)
    res = []

    Try(0)

if __name__ == '__main__':
    main()
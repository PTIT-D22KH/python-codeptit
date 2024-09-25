# pykt067.py
def Try(i,n, a, res, used):
    for j in range(1, n + 1):
        if not used[j]:
            a[i] = j
            # print(a)
            used[j] = True
            if i == n - 1:
                res.append(a[:])
            else:
                Try(i + 1, n, a, res, used)
            used[j] = False

            
def main():
    # Write your code here
    for _ in range(int(input())):
        n = int(input())
        res = []
        a = [0] * n
        used = [False] * (n + 1)
        Try(0, n, a, res, used)
        res.sort(reverse = True)
        print(len(res))
        for x in res:
            print(''.join(map(str, x)), end = ' ')
        print()



if __name__ == '__main__':
    main()

def main():
    n, m = [int(i) for i in input().split()]
    a = []
    for i in range(n):
        x = [int(i) for i in input().split()]
        a.append(x)
    
    if n < m:
        d = [1]
        while m > n + len(d):
            d.append(d[-1] + 2)
        for i in range(n):
            for j in range(m):
                if not (j in d):
                    print(a[i][j], end=' ')
            print()
    else:
        d = []
        if n > m:
            d = [0]
        while n > m + len(d):
            d.append(d[-1] + 2)
        for i in range(n):
            if not (i in d):
                for j in range(m):
                    print(a[i][j], end=' ')
                print()

if __name__ == '__main__':
    main()
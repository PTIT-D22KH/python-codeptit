# py02021.py

def main():
    # Write your code here
    for t in range(int(input())):
        n, m, p = [int(i) for i in input().split()]
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        c = [int(i) for i in input().split()]
        i = 0
        j = 0
        k = 0
        ok = False
        while (i < n and j < m and k < p):
            if (a[i] == b[j] and b[j] == c[k]):
                print(a[i], end = ' ')
                ok = True
                i += 1
                j += 1
                k += 1

            elif a[i] < b[j]:
                i += 1
            elif b[j] < c[k]:
                j += 1
            else:
                k += 1
        if (ok == False):
            print("NO")
        print()

if __name__ == '__main__':
    main()

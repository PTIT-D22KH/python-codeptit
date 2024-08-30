# py02012.py

def main():
    # Write your code here
    n = int(input())
    s = []
    while True:
        try:
            s += [int(i) for i in input().split()]
        except:
            break

    a = []
    b = []
    for x in s:
        if (x % 2 == 0):
            a.append(int(x))
        else:
            b.append(int(x))
        
    a.sort()
    b.sort(key = lambda x: -x)
    i = 0
    j = 0
    for x in s:
        if (x % 2 == 0):
            print(a[i], end = ' ')
            i += 1
        else:
            print(b[j], end = ' ')
            j += 1



if __name__ == '__main__':
    main()

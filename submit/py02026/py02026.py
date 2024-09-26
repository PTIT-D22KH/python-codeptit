# py02026.py

def main():
    # Write your code here
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    n = len(a)
    m = len(b)
    if n != m:
        print("NO")
    else:
        
        for i in range(len(a)):
            if a[i] != b[i]:
                print("NO")
                return
        print("YES")

if __name__ == '__main__':
    main()

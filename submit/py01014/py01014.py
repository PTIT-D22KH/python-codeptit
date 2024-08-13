# py01014.py

def main():
    # Write your code here
    a, k, n = [int(i) for i in input().split()]
    i = k - (a % k)
    n -= a
    b = []
    while(i <= n):
        b.append(i)
        i += k
    if (len(b) == 0):
        print("-1")
    else:
        for i in b:
            print(i, end = " ")
        

if __name__ == '__main__':
    main()

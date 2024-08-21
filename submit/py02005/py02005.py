# py02005.py

def main():
    # Write your code here
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if (a[i] > a[j]):
                count += 1
    print(count)            

if __name__ == '__main__':
    main()

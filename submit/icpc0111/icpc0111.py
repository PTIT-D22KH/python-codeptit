def main():
    # Write your code here
    for _ in range(int(input())):
        n, d = [int(i) for i in input().split()]
        a = [int(i) for i in input().split()]
        d = d % n  
        for i in range(n):
            print(a[(i + d) % n], end=' ')
        print()

if __name__ == '__main__':
    main()
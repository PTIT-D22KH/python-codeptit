# py02051.py

def main():
    # Write your code here
    n = int(input())
    b = []
    for i in range(n):
        temp = [int(i) for i in input().split()]
        b.append(temp)
    # print(a)
    a = [0] * n
    if n == 2:
        a[0] = b[0][1] // 2
        a[1] = b[0][1] // 2
    else:
        a[0] = (b[0][1] + b[0][2] - b[1][2]) // 2
        for i in range(1, n):
            a[i] = b[0][i] - a[0]
    for x in a:
        print(x, end = ' ')

if __name__ == '__main__':
    main()

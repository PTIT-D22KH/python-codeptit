# py02038.py

def main():
    # Write your code here
    n = int(input())
    a = []
    for _ in range(n):
        s = input()
        a.append(s)
    res = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if a[i][j] == 'C':
                count += 1
        if count > 1:
            res += count  * (count - 1) // 2
    for j in range(n):
        count  = 0
        for i in range(n):
            if a[i][j] == 'C':
                count += 1
        if count > 1:
            res += count * (count - 1) // 2
    print(res)
            

if __name__ == '__main__':
    main()

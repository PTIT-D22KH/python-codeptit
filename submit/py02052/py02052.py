# py02052.py

def main():
    # Write your code here
    n = int(input())
    a = []
    for i in range(n):
        x = [int(i) for i in input().split()]
        a.append(x)
    k = int(input())
    # print(a)
    upperSum = 0
    lowerSum = 0
    for i in range(n):
        for j in range(n):
            if j < i:
                lowerSum += a[i][j]
            elif j > i:
                upperSum += a[i][j]
    res = abs(upperSum - lowerSum)
    if res <= k:
        print("YES") 
        
    else:
        print("NO")
    print(res)

if __name__ == '__main__':
    main()

# py02039.py

def main():
    # Write your code here
    n = int(input())
    a = []
    for i in range(n):
        x = [int(i) for i in input().split()]
        a.append(x)
    k = int(input())
    firstHalf = 0
    secondHalf  = 0
    for i in range(n):
        for j in range(n):
            if j < n - i - 1:
                firstHalf += a[i][j]
                # print(firstHalf)
            elif j > n - i - 1 :
                secondHalf += a[i][j]
    res = abs(firstHalf - secondHalf) 
    
    if(res <= k):
        print("YES")
    else:
        print("NO")

    print(res)

if __name__ == '__main__':
    main()
